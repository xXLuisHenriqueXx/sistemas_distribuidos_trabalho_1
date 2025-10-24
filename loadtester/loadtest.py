import asyncio
import aiohttp
import os
import time
import datetime
from dotenv import load_dotenv

# Importa dos novos módulos
from monitor import ContainerMonitor
from worker import worker
from reporting import calculate_stats, append_results_to_markdown

load_dotenv()

# --- Configuração ---
# Carrega todas as configurações do ambiente
URL = os.getenv("TARGET_URL", "http://app:3000")
DURATION = int(os.getenv("DURATION", "60"))
CONCURRENCY = int(os.getenv("CONCURRENCY", "100"))
DATASET_SIZE = int(os.getenv("DATASET_SIZE", "50000"))
MONITOR_TARGET = os.getenv("MONITOR_TARGET", "app")
REPORT_INTERVAL = int(os.getenv("REPORT_INTERVAL", "15"))
DB_TYPE = os.getenv("DB_TYPE", "postgres")
USE_INDEX = os.getenv("USE_INDEX", "false").lower() == 'true' # Garante booleano

READ_RATIO = float(os.getenv("READ_RATIO", "0.5"))

# --- Globais para o estado do teste ---
# Estas listas e contadores são compartilhados entre workers e reporters
read_latencies = []
write_latencies = []

errors_read = 0
errors_write = 0

start_time = None
post_ids = []
post_ids_lock = asyncio.Lock() # Lock para acesso seguro à lista post_ids
periodic_reports = []

# --- Reporter Periódico ---
async def periodic_reporter(monitor):
    """Coleta e imprime estatísticas periodicamente durante o teste."""
    global periodic_reports
    last_total_count = 0

    # Espera start_time ser definido antes de começar
    while start_time is None:
        await asyncio.sleep(0.1)

    while time.time() - start_time < DURATION:
        await asyncio.sleep(REPORT_INTERVAL)

        # Copia listas para cálculo seguro (evita race condition simples)
        current_read_latencies = list(read_latencies)
        current_write_latencies = list(write_latencies)

        read_stats = calculate_stats(current_read_latencies)
        write_stats = calculate_stats(current_write_latencies)

        total_count = read_stats['count'] + write_stats['count']
        # Copia contadores de erro para leitura segura
        current_errors_read = errors_read
        current_errors_write = errors_write
        total_errors = current_errors_read + current_errors_write

        delta = total_count - last_total_count
        last_total_count = total_count

        duration_so_far = time.time() - start_time
        summary = monitor.summary() # Pega métricas atuais do monitor

        report_data = {
            "time_s": int(duration_so_far),
            "new_reqs": delta,
            "read_avg_ms": read_stats['avg_ms'],
            "read_p95_ms": read_stats['p95_ms'],
            "read_p99_ms": read_stats['p99_ms'],
            "write_avg_ms": write_stats['avg_ms'],
            "write_p95_ms": write_stats['p95_ms'],
            "write_p99_ms": write_stats['p99_ms'],
            "cpu_avg_pct": summary['cpu_avg'],
            "mem_avg_mb": summary['mem_avg']
        }
        periodic_reports.append(report_data)

        # Imprime o relatório no console
        print(f"\n[+{int(duration_so_far)}s] Progress report:")
        print(f"  Total requests: {total_count} (+{delta} in last {REPORT_INTERVAL}s)")
        print(f"  Total errors: {total_errors} (R:{current_errors_read}, W:{current_errors_write})")
        print(f"  Read (avg/p95/p99): {read_stats['avg_ms']:.2f} / {read_stats['p95_ms']:.2f} / {read_stats['p99_ms']:.2f} ms ({read_stats['count']})")
        print(f"  Write (avg/p95/p99): {write_stats['avg_ms']:.2f} / {write_stats['p95_ms']:.2f} / {write_stats['p99_ms']:.2f} ms ({write_stats['count']})")
        print(f"  CPU avg/max: {summary['cpu_avg']:.2f}% / {summary['cpu_max']:.2f}%")
        print(f"  Mem avg/max: {summary['mem_avg']:.2f} MB / {summary['mem_max']:.2f} MB")
        print(f"  Net TX/RX: {summary['net_tx']:.2f} MB / {summary['net_rx']:.2f} MB")
        print("--------------------------------------------------")

# --- Função Principal ---
async def main():
    """Orquestra o teste de carga."""
    global start_time, periodic_reports, post_ids
    global errors_read, errors_write

    # Reseta estado global para garantir execução limpa
    periodic_reports = []
    post_ids = []
    read_latencies.clear()
    write_latencies.clear()
    errors_read = 0
    errors_write = 0
    start_time = None # Garante que start_time é None no início

    # --- Cálculo das Proporções Reais ---
    read_ratio_actual = READ_RATIO
    # Garante que a soma não exceda 1.0
    if read_ratio_actual > 1.0:
        print("ERRO: READ_RATIO excede 1.0")
        return
    write_ratio_actual = 1.0 - read_ratio_actual

    # Boundaries para a lógica do worker
    read_boundary = read_ratio_actual

    # --- String de Configuração para Logs ---
    load_mix_str = f"{read_ratio_actual*100:.0f}% Read_ID, {write_ratio_actual*100:.0f}% Write"

    config_data = {
        "DB_TYPE": DB_TYPE,
        "USE_INDEX": USE_INDEX,
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

    try:
        monitor = ContainerMonitor(MONITOR_TARGET)
    except RuntimeError as e:
        print(f"Error initializing monitor: {e}")
        return

    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        print(f"Pre-carregando lista de IDs do {DB_TYPE.upper()}...")
        try:
            preheat_timeout = aiohttp.ClientTimeout(total=max(60, DURATION))
            async with session.get(f"{URL}/posts/all/ids", timeout=preheat_timeout) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    async with post_ids_lock:
                        if DB_TYPE == "postgres":
                            post_ids = [item['id'] for item in data if 'id' in item]
                        else:
                            post_ids = [item['_id'] for item in data if '_id' in item]
                    print(f"Lista de IDs pré carregados com {len(post_ids)} IDs.")
                    if not post_ids:
                         print("AVISO: Lista de IDs veio vazia!")
                else:
                    print(f"ERRO: Falha ao pré carregar IDs (Status: {resp.status}). O teste de leitura pode falhar.")
        except asyncio.TimeoutError:
             print("ERRO CRÍTICO: Timeout durante o pré carregamento da lista de IDs. Encerrando.")
             return
        except Exception as e:
            print(f"ERRO CRÍTICO no pré carregamento: {e}. Encerrando.")
            return

        if not post_ids:
            print("ERRO CRÍTICO: Não foi possível obter IDs para o teste. Encerrando.")
            return

        # --- Início Efetivo do Teste ---
        print("Iniciando workers...")
        start_time = time.time() # Define o tempo de início AQUI

        # Cria tarefas de monitoramento e reportagem
        monitor_task = asyncio.create_task(monitor.collect_metrics())
        reporter_task = asyncio.create_task(periodic_reporter(monitor))

        # Cria e inicia os workers
        # Passa referências para as listas globais e contadores de erro
        worker_tasks = []
        for i in range(CONCURRENCY):
            task = asyncio.create_task(worker(
                session, i, read_boundary,
                URL, DURATION, DB_TYPE, DATASET_SIZE, start_time, # Configs
                post_ids_lock, post_ids, # Estado compartilhado
                read_latencies, write_latencies, # Listas de latência
                # Passando funções lambda para incrementar erros de forma segura (alternativa a locks)
                lambda: globals().update(errors_read=errors_read + 1),
                lambda: globals().update(errors_write=errors_write + 1)
            ))
            worker_tasks.append(task)

        # Espera todos os workers terminarem
        await asyncio.gather(*worker_tasks)
        print("Workers concluídos.")

    # --- Finalização e Coleta de Resultados ---
    monitor.running = False # Sinaliza para o monitor parar
    # Dá um tempo para as últimas métricas serem coletadas
    await asyncio.sleep(2)

    # Cancela tarefas de fundo
    monitor_task.cancel()
    reporter_task.cancel()

    # Espera cancelamento concluir
    try:
        await monitor_task
    except asyncio.CancelledError:
        pass
    try:
        await reporter_task
    except asyncio.CancelledError:
        pass
    except TypeError: # Ignora o TypeError que ocorria no shutdown
         print("Ignorando TypeError no reporter durante o shutdown.")
         pass

    # Calcula duração final
    duration_final = time.time() - start_time
    # Pega o resumo final do monitor
    summary_final = monitor.summary()

    # --- Cálculo Final das Estatísticas ---
    read_stats = calculate_stats(read_latencies)
    write_stats = calculate_stats(write_latencies)

    total_requests = read_stats['count'] + write_stats['count']
    total_errors = errors_read + errors_write
    req_per_sec = total_requests / duration_final if duration_final > 0 else 0

    results_data = {
        "total_requests": total_requests,
        "total_errors": total_errors,
        "errors_read": errors_read,
        "errors_write": errors_write,
        "duration_s": duration_final,
        "req_per_sec": req_per_sec,

        "read_reqs": read_stats['count'],
        "read_avg_ms": read_stats['avg_ms'],
        "read_p95_ms": read_stats['p95_ms'],
        "read_p99_ms": read_stats['p99_ms'],

        "write_reqs": write_stats['count'],
        "write_avg_ms": write_stats['avg_ms'],
        "write_p95_ms": write_stats['p95_ms'],
        "write_p99_ms": write_stats['p99_ms'],
    }

    # --- Impressão Final no Console ---
    print("\n=== FINAL RESULTS ===")
    print(f"DB Type: {DB_TYPE.upper()} (Indexes: {USE_INDEX})")
    print(f"Total requests: {total_requests} | Req/sec: {req_per_sec:.2f}")
    print(f"Total errors: {total_errors} (R:{errors_read}, W:{errors_write})")
    print("----------------")
    print(f"Read (Prim)  : {read_stats['count']} reqs | avg: {read_stats['avg_ms']:.2f}ms | p95: {read_stats['p95_ms']:.2f}ms | p99: {read_stats['p99_ms']:.2f}ms")
    print(f"Write        : {write_stats['count']} reqs | avg: {write_stats['avg_ms']:.2f}ms | p95: {write_stats['p95_ms']:.2f}ms | p99: {write_stats['p99_ms']:.2f}ms")
    print("----------------")
    print(f"CPU avg/max: {summary_final['cpu_avg']:.2f}% / {summary_final['cpu_max']:.2f}%")
    print(f"Memory avg/max: {summary_final['mem_avg']:.2f} MB / {summary_final['mem_max']:.2f} MB")
    print(f"Network TX/RX: {summary_final['net_tx']:.2f} MB / {summary_final['net_rx']:.2f} MB")
    print("================")

    # --- Salva Resultados no Arquivo ---
    append_results_to_markdown(config_data, results_data, summary_final, periodic_reports)

# --- Ponto de Entrada ---
if __name__ == "__main__":
    start_time = None # Garante que start_time é None antes de rodar main
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nTeste interrompido pelo usuário.")
    # Adiciona um finally para garantir que start_time seja resetado se ocorrer erro
    finally:
        start_time = None

