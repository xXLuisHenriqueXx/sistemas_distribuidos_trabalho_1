import asyncio
import aiohttp
import os
import random
import statistics
import time
import docker
import datetime
from dotenv import load_dotenv

load_dotenv()

# --- Configuração ---
URL = os.getenv("TARGET_URL", "http://app:3000")
DURATION = int(os.getenv("DURATION", "30"))
CONCURRENCY = int(os.getenv("CONCURRENCY", "100"))
DATASET_SIZE = int(os.getenv("DATASET_SIZE", "50000"))
MONITOR_TARGET = os.getenv("MONITOR_TARGET", "app")
REPORT_INTERVAL = int(os.getenv("REPORT_INTERVAL", "10")) 
DB_TYPE = os.getenv("DB_TYPE", "postgres")
USE_INDEX = os.getenv("USE_INDEX", "unknown") 

ENABLE_SECONDARY_READS = os.getenv("ENABLE_SECONDARY_READS", "true").lower() == "true"
READ_RATIO = float(os.getenv("READ_RATIO", "0.4")) 
SECONDARY_READ_RATIO = float(os.getenv("SECONDARY_READ_RATIO", "0.1")) 

# --- Globais para o teste (MODIFICADAS) ---
# Substituímos 'latencies' e 'errors' por listas discriminadas
read_latencies = []
secondary_read_latencies = []
write_latencies = []

errors_read = 0
errors_secondary = 0
errors_write = 0

start_time = None
post_ids = [] 
post_ids_lock = asyncio.Lock()
periodic_reports = [] 

LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
    "adipcing", "elit", "sed", "do", "eiusmod", "tempor",
    "incididunt", "ut", "labore", "et", "dolore", "magna",
    "culpa", "qui", "officia", "deserunt", "mollit", "anim",
    "id", "est", "laborum"
]

# ---------- Monitor Docker (Sem alterações) ----------
class ContainerMonitor:
    def __init__(self, target_name):
        self.client = docker.from_env()
        self.target_name = target_name
        self.cpu_samples = []
        self.mem_samples = []
        self.net_tx = 0
        self.net_rx = 0
        self.running = True

    def get_container(self):
        containers = self.client.containers.list()
        for c in containers:
            if self.target_name in c.name:
                return c
        raise RuntimeError(f"Container '{self.target_name}' not found")

    async def collect_metrics(self, interval=1.0):
        container = self.get_container()
        prev_cpu = prev_system = None

        while self.running:
            try:
                stats = container.stats(stream=False)
                cpu_total = stats["cpu_stats"]["cpu_usage"]["total_usage"]
                system_cpu = stats["cpu_stats"]["system_cpu_usage"]
                online_cpus = stats["cpu_stats"].get("online_cpus", 1)

                if prev_cpu is not None:
                    cpu_delta = cpu_total - prev_cpu
                    system_delta = system_cpu - prev_system
                    cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0 if system_delta > 0 else 0
                    self.cpu_samples.append(cpu_percent)

                prev_cpu = cpu_total
                prev_system = system_cpu

                mem_usage = stats["memory_stats"]["usage"] / (1024 * 1024)
                self.mem_samples.append(mem_usage)

                if "networks" in stats:
                    tx = sum(n["tx_bytes"] for n in stats["networks"].values())
                    rx = sum(n["rx_bytes"] for n in stats["networks"].values())
                    self.net_tx = tx
                    self.net_rx = rx
            except Exception:
                pass 

            await asyncio.sleep(interval)

    def summary(self):
        return {
            "cpu_avg": statistics.mean(self.cpu_samples) if self.cpu_samples else 0,
            "cpu_max": max(self.cpu_samples) if self.cpu_samples else 0,
            "mem_avg": statistics.mean(self.mem_samples) if self.mem_samples else 0,
            "mem_max": max(self.mem_samples) if self.mem_samples else 0,
            "net_tx": self.net_tx / (1024 * 1024),
            "net_rx": self.net_rx / (1024 * 1024),
        }

# --- NOVA FUNÇÃO AUXILIAR ---
def calculate_stats(lat_list):
    """Calcula estatísticas para uma lista de latências."""
    if not lat_list:
        return {'avg_ms': 0, 'p95_ms': 0, 'p99_ms': 0, 'count': 0}
    
    count = len(lat_list)
    avg = statistics.mean(lat_list)
    
    # p95/p99 só são significativos com > 100 amostras
    if count > 100:
        quantiles_list = statistics.quantiles(lat_list, n=100)
        p95 = quantiles_list[94]
        p99 = quantiles_list[98]
    else:
        # Retorna a média se não houver dados suficientes
        p95 = avg
        p99 = avg
        
    return {
        'avg_ms': avg * 1000,
        'p95_ms': p95 * 1000,
        'p99_ms': p99 * 1000,
        'count': count
    }

# --- Função de Log (MODIFICADA) ---
def append_results_to_markdown(config, results, summary, periodic_data, filename="test_results.md"):
    """Anexa os resultados discriminados ao markdown."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"## 🧪 Test Run: {timestamp}\n\n")
            
            f.write("### ⚙️ Configuration\n")
            f.write("| Parameter | Value |\n")
            f.write("| :--- | :--- |\n")
            for key, val in config.items():
                f.write(f"| **{key}** | {val} |\n")
            f.write("\n")
            
            # --- Tabela de Performance Modificada ---
            f.write("### 📊 Performance Results (Final)\n")
            f.write(f"**Total Requests:** {results['total_requests']} | **Total Errors:** {results['total_errors']} | **Req/Sec:** {results['req_per_sec']:.2f}\n\n")
            
            f.write("| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            f.write(f"| **Read (Primary)** | {results['read_reqs']} | {results['errors_read']} | {results['read_avg_ms']:.2f} | {results['read_p95_ms']:.2f} | {results['read_p99_ms']:.2f} |\n")
            if config['ENABLE_SECONDARY_READS']:
                f.write(f"| **Read (Secondary)** | {results['secondary_reqs']} | {results['errors_secondary']} | {results['secondary_avg_ms']:.2f} | {results['secondary_p95_ms']:.2f} | {results['secondary_p99_ms']:.2f} |\n")
            f.write(f"| **Write** | {results['write_reqs']} | {results['errors_write']} | {results['write_avg_ms']:.2f} | {results['write_p95_ms']:.2f} | {results['write_p99_ms']:.2f} |\n")
            f.write("\n")
            
            # --- Tabela de Recursos (Sem alteração) ---
            f.write(f"### 💻 Resource Usage ({config['MONITOR_TARGET']} - Final)\n")
            f.write("| Resource | Avg | Max |\n")
            f.write("| :--- | :--- | :--- |\n")
            f.write(f"| **CPU (%)** | {summary['cpu_avg']:.2f} | {summary['cpu_max']:.2f} |\n")
            f.write(f"| **Memory (MB)** | {summary['mem_avg']:.2f} | {summary['mem_max']:.2f} |\n")
            f.write(f"| **Net TX (MB)** | - | {summary['net_tx']:.2f} |\n")
            f.write(f"| **Net RX (MB)** | - | {summary['net_rx']:.2f} |\n")
            f.write("\n")

            # --- Tabela Periódica Modificada ---
            f.write("### 📈 Periodic Report Log\n")
            f.write("| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            if not periodic_data:
                f.write("| N/A | N/A | N/A | N/A | N/A | N/A | N/A |\n")
            else:
                for report in periodic_data:
                    # Lida com o caso de leituras secundárias desabilitadas
                    sec_avg = f"{report['secondary_avg_ms']:.2f}" if config['ENABLE_SECONDARY_READS'] else "N/A"
                    f.write(f"| {report['time_s']} | {report['new_reqs']} | {report['read_avg_ms']:.2f} | {sec_avg} | {report['write_avg_ms']:.2f} | {report['cpu_avg_pct']:.2f} | {report['mem_avg_mb']:.2f} |\n")
            
            f.write("\n---\n\n")

        print(f"\n✅ Resultados anexados em: {filename}")
    except Exception as e:
        print(f"❌ Falha ao salvar resultados no arquivo: {e}")

# Função auxiliar para gerar Lorem Ipsum (Sem alterações)
def generate_lorem_ipsum(max_words=100):
    num_words = random.randint(1, max_words)
    content = " ".join(random.choices(LOREM_WORDS, k=num_words))
    return content.capitalize() + "."

# ---------- Lógica do Load test (MODIFICADA) ----------
async def worker(session, wid, read_boundary, secondary_read_boundary):
    global errors_read, errors_secondary, errors_write, post_ids
    
    while time.time() - start_time < DURATION:
        t0 = time.time()
        op_roll = random.random()
        try:
            if op_roll < read_boundary:
                # --- Requisição GET Primária (Leitura por ID) ---
                pid = None
                async with post_ids_lock:
                    if post_ids:
                        pid = random.choice(post_ids)
                
                if pid:
                    async with session.get(f"{URL}/posts/{pid}") as resp:
                        await resp.text()
                        resp.raise_for_status() # Lança erro se for 4xx/5xx
                    read_latencies.append(time.time() - t0) # Adiciona à lista correta
                else:
                    await asyncio.sleep(0.01)
                    continue 
            
            elif op_roll < secondary_read_boundary:
                # --- Requisição GET Secundária (Leitura por user_id) ---
                uid = random.randint(1, 1000) 
                async with session.get(f"{URL}/users/{uid}/posts") as resp:
                    await resp.text()
                    resp.raise_for_status()
                secondary_read_latencies.append(time.time() - t0) # Adiciona à lista correta

            else:
                # --- Requisição POST (Escrita) ---
                payload = {}
                if DB_TYPE == "postgres":
                    payload = { "user_id": random.randint(1, 1000), "title": "...", "content": "..." }
                else:
                    payload = { "author": { "user_id": random.randint(1, 1000), "username": "..." }, "title": "...", "content": "..." }
                
                async with session.post(f"{URL}/posts", json=payload) as resp:
                    await resp.text()
                    resp.raise_for_status()
                write_latencies.append(time.time() - t0) # Adiciona à lista correta

            # latencies.append(time.time() - t0) # <-- Removido
        except Exception as e:
            # Incrementa o contador de erro correto
            if op_roll < read_boundary:
                errors_read += 1
            elif op_roll < secondary_read_boundary:
                errors_secondary += 1
            else:
                errors_write += 1
        
        await asyncio.sleep(0.001)

# ---------- Reporter (MODIFICADO) ----------
async def periodic_reporter(monitor):
    global periodic_reports 
    last_count = 0
    
    while time.time() - start_time < DURATION:
        await asyncio.sleep(REPORT_INTERVAL)

        # Calcula estatísticas para cada tipo
        read_stats = calculate_stats(read_latencies)
        secondary_stats = calculate_stats(secondary_read_latencies)
        write_stats = calculate_stats(write_latencies)
        
        total_count = read_stats['count'] + secondary_stats['count'] + write_stats['count']
        total_errors = errors_read + errors_secondary + errors_write
        
        delta = total_count - last_count
        last_count = total_count

        duration = time.time() - start_time
        summary = monitor.summary()
        
        # Armazena os dados discriminados
        report_data = {
            "time_s": int(duration),
            "new_reqs": delta,
            "read_avg_ms": read_stats['avg_ms'],
            "read_p95_ms": read_stats['p95_ms'],
            "secondary_avg_ms": secondary_stats['avg_ms'],
            "secondary_p95_ms": secondary_stats['p95_ms'],
            "write_avg_ms": write_stats['avg_ms'],
            "write_p95_ms": write_stats['p95_ms'],
            "cpu_avg_pct": summary['cpu_avg'],
            "mem_avg_mb": summary['mem_avg']
        }
        periodic_reports.append(report_data)

        # Imprime os dados discriminados
        print(f"\n[+{int(duration)}s] Progress report:")
        print(f"  Total requests: {total_count} (+{delta} in last {REPORT_INTERVAL}s)")
        print(f"  Total errors: {total_errors} (R:{errors_read}, S:{errors_secondary}, W:{errors_write})")
        print(f"  Read (avg/p95): {read_stats['avg_ms']:.2f} ms / {read_stats['p95_ms']:.2f} ms")
        if ENABLE_SECONDARY_READS:
             print(f"  Sec.Read (avg/p95): {secondary_stats['avg_ms']:.2f} ms / {secondary_stats['p95_ms']:.2f} ms")
        print(f"  Write (avg/p95): {write_stats['avg_ms']:.2f} ms / {write_stats['p95_ms']:.2f} ms")
        print(f"  CPU avg/max: {summary['cpu_avg']:.2f}% / {summary['cpu_max']:.2f}%")
        print(f"  Mem avg/max: {summary['mem_avg']:.2f} MB / {summary['mem_max']:.2f} MB")
        print(f"  Net TX/RX: {summary['net_tx']:.2f} MB / {summary['net_rx']:.2f} MB")
        print("--------------------------------------------------")

# ---------- Main (MODIFICADO) ----------
async def main():
    global start_time, periodic_reports, post_ids
    global errors_read, errors_secondary, errors_write
    
    # Reseta os contadores globais a cada execução
    periodic_reports = [] 
    post_ids = []
    read_latencies.clear()
    secondary_read_latencies.clear()
    write_latencies.clear()
    errors_read = 0
    errors_secondary = 0
    errors_write = 0
    
    # --- Lógica de proporção (Sem alteração) ---
    read_ratio_actual = READ_RATIO
    secondary_read_ratio_actual = 0.0
    
    if ENABLE_SECONDARY_READS:
        secondary_read_ratio_actual = SECONDARY_READ_RATIO
        
    write_ratio_actual = 1.0 - read_ratio_actual - secondary_read_ratio_actual
    
    read_boundary = read_ratio_actual
    secondary_read_boundary = read_ratio_actual + secondary_read_ratio_actual
    
    load_mix_str = f"{read_ratio_actual*100:.0f}% Read_ID, {write_ratio_actual*100:.0f}% Write"
    if ENABLE_SECONDARY_READS:
        load_mix_str = f"{read_ratio_actual*100:.0f}% Read_ID, {secondary_read_ratio_actual*100:.0f}% Read_User, {write_ratio_actual*100:.0f}% Write"
    
    config_data = {
        "DB_TYPE": DB_TYPE,
        "USE_INDEX": USE_INDEX,
        "ENABLE_SECONDARY_READS": ENABLE_SECONDARY_READS,
        "DATASET_SIZE": DATASET_SIZE,
        "CONCURRENCY": CONCURRENCY,
        "DURATION_S": DURATION,
        "LOAD_MIX": load_mix_str,
        "MONITOR_TARGET": MONITOR_TARGET,
        "APP_CPUS": os.getenv("APP_CPUS", "N/A"),
        "APP_MEM": os.getenv("APP_MEM", "N/A"),
    }

    print(f"Starting load test on {DB_TYPE.upper()}:")
    print(f"  {CONCURRENCY} clients, {DURATION}s duration")
    print(f"  Load Mix: {config_data['LOAD_MIX']}")
    print(f"  Indexes: {USE_INDEX}")
    print(f"  Secondary Reads: {'ENABLED' if ENABLE_SECONDARY_READS else 'DISABLED'}")
    
    try:
        monitor = ContainerMonitor(MONITOR_TARGET)
    except RuntimeError as e:
        print(f"Error: {e}")
        return

    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        
        # --- ETAPA DE PRÉ-AQUECIMENTO (Sem alteração) ---
        print(f"Pre-aquecendo lista de IDs do {DB_TYPE.upper()}...")
        try:
            async with session.get(f"{URL}/posts/all/ids") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    async with post_ids_lock:
                        if DB_TYPE == "postgres":
                            post_ids = [item['id'] for item in data]
                        else:
                            post_ids = [item['_id'] for item in data]
                    print(f"Lista de IDs pré-aquecida com {len(post_ids)} IDs.")
                else:
                    print(f"ERRO: Falha ao pré-aquecer IDs (Status: {resp.status}). O teste de leitura falhará.")
        except Exception as e:
            print(f"ERRO CRÍTICO no pré-aquecimento: {e}. Encerrando.")
            return

        # --- INÍCIO DO TESTE (Sem alteração) ---
        start_time = time.time()
        
        monitor_task = asyncio.create_task(monitor.collect_metrics())
        reporter_task = asyncio.create_task(periodic_reporter(monitor))

        tasks = [asyncio.create_task(worker(session, i, read_boundary, secondary_read_boundary)) for i in range(CONCURRENCY)]
        await asyncio.gather(*tasks)

    monitor.running = False
    await asyncio.sleep(1) 

    if not reporter_task.done():
        reporter_task.cancel()

    duration = time.time() - start_time
    try:
        await monitor_task
    except asyncio.CancelledError:
        pass 

    summary = monitor.summary()

    # --- Cálculo de resultados (MODIFICADO) ---
    read_stats = calculate_stats(read_latencies)
    secondary_stats = calculate_stats(secondary_read_latencies)
    write_stats = calculate_stats(write_latencies)
    
    total_requests = read_stats['count'] + secondary_stats['count'] + write_stats['count']
    total_errors = errors_read + errors_secondary + errors_write
    req_per_sec = total_requests / duration if duration > 0 else 0
    
    results_data = {
        "total_requests": total_requests,
        "total_errors": total_errors,
        "errors_read": errors_read,
        "errors_secondary": errors_secondary,
        "errors_write": errors_write,
        "duration_s": duration,
        "req_per_sec": req_per_sec,
        
        "read_reqs": read_stats['count'],
        "read_avg_ms": read_stats['avg_ms'],
        "read_p95_ms": read_stats['p95_ms'],
        "read_p99_ms": read_stats['p99_ms'],
        
        "secondary_reqs": secondary_stats['count'],
        "secondary_avg_ms": secondary_stats['avg_ms'],
        "secondary_p95_ms": secondary_stats['p95_ms'],
        "secondary_p99_ms": secondary_stats['p99_ms'],
        
        "write_reqs": write_stats['count'],
        "write_avg_ms": write_stats['avg_ms'],
        "write_p95_ms": write_stats['p95_ms'],
        "write_p99_ms": write_stats['p99_ms'],
    }

    # --- Print final (MODIFICADO) ---
    print("\n=== FINAL RESULTS ===")
    print(f"DB Type: {DB_TYPE.upper()} (Indexes: {USE_INDEX})")
    print(f"Total requests: {total_requests} | Req/sec: {req_per_sec:.2f}")
    print(f"Total errors: {total_errors} (R:{errors_read}, S:{errors_secondary}, W:{errors_write})")
    print("----------------")
    print(f"Read (Prim)  : {read_stats['count']} reqs | avg: {read_stats['avg_ms']:.2f}ms | p95: {read_stats['p95_ms']:.2f}ms | p99: {read_stats['p99_ms']:.2f}ms")
    if ENABLE_SECONDARY_READS:
        print(f"Read (Sec)   : {secondary_stats['count']} reqs | avg: {secondary_stats['avg_ms']:.2f}ms | p95: {secondary_stats['p95_ms']:.2f}ms | p99: {secondary_stats['p99_ms']:.2f}ms")
    print(f"Write        : {write_stats['count']} reqs | avg: {write_stats['avg_ms']:.2f}ms | p95: {write_stats['p95_ms']:.2f}ms | p99: {write_stats['p99_ms']:.2f}ms")
    print("----------------")
    print(f"CPU avg/max: {summary['cpu_avg']:.2f}% / {summary['cpu_max']:.2f}%")
    print(f"Memory avg/max: {summary['mem_avg']:.2f} MB / {summary['mem_max']:.2f} MB")
    print(f"Network TX/RX: {summary['net_tx']:.2f} MB / {summary['net_rx']:.2f} MB")
    print("================")

    append_results_to_markdown(config_data, results_data, summary, periodic_reports)

if __name__ == "__main__":
    asyncio.run(main())