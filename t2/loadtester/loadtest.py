import os
import time
import requests
import concurrent.futures
import random
import datetime
import statistics
import sys

# --- CONFIGURAÇÕES ---
TARGET_URL = os.getenv("TARGET_URL", "http://app:3000")
DURATION = int(os.getenv("DURATION", "45"))
CONCURRENCY = int(os.getenv("CONCURRENCY", "5"))
READ_RATIO = float(os.getenv("READ_RATIO", "0.8"))
OUTPUT_FILE = "/app/reports/relatorio_experimento.md"

ENV_CONFIGS = {
    "READ_PREFERENCE": os.getenv("READ_PREFERENCE", "N/A"),
    "WRITE_CONCERN": os.getenv("WRITE_CONCERN", "N/A"),
    "CHAOS_FAILURE_CHANCE": os.getenv("CHAOS_FAILURE_CHANCE", "N/A"),
    "DATASET_SIZE": os.getenv("DATASET_SIZE", "N/A"),
    "COMPLEX_DOC_RATIO": os.getenv("COMPLEX_DOC_RATIO", "N/A"),
}

reads_results = []
writes_results = []

def wait_for_server():
    """Aguarda o servidor estar pronto (Health Check) antes de iniciar"""
    print(f"⏳ Aguardando servidor ficar pronto em {TARGET_URL}/health ...")
    
    max_retries = 300 
    for i in range(max_retries):
        try:
            resp = requests.get(f"{TARGET_URL}/health", timeout=1)
            if resp.status_code == 200:
                print("\n✅ Servidor pronto! Iniciando carga.")
                return
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            print(f"Ignorando erro de warmup: {e}")
            
        print(".", end="", flush=True)
        time.sleep(1)
    
    print("\n❌ Timeout: Servidor não subiu a tempo. Abortando.")
    sys.exit(1)

def do_read():
    start = time.perf_counter()
    timestamp = time.time()
    error = False
    code = 0
    try:
        resp = requests.get(f"{TARGET_URL}/orders/by-status/PAID?limit=5", timeout=2)
        code = resp.status_code
        if code >= 400:
            error = True
    except Exception as e:
        error = True
        code = 0 
    
    latency = (time.perf_counter() - start) * 1000
    return {"timestamp": timestamp, "latency": latency, "error": error, "code": code}

def do_write():
    start = time.perf_counter()
    timestamp = time.time()
    error = False
    code = 0
    payload = {
        "user_id": random.randint(1, 1000),
        "status": "PENDING",
        "total_value": random.uniform(10, 500),
        "created_at": datetime.datetime.now().isoformat(),
        "items": [{"sku": "TEST-LOAD", "qty": 1}]
    }
    try:
        resp = requests.post(f"{TARGET_URL}/orders", json=payload, timeout=2)
        code = resp.status_code
        if code >= 400:
            error = True
    except Exception as e:
        error = True
        code = 0
    
    latency = (time.perf_counter() - start) * 1000
    return {"timestamp": timestamp, "latency": latency, "error": error, "code": code}

def worker():
    start_time = time.time()
    while (time.time() - start_time) < DURATION:
        is_read = random.random() < READ_RATIO
        if is_read:
            res = do_read()
            reads_results.append(res)
        else:
            res = do_write()
            writes_results.append(res)
        time.sleep(0.01) 

def calculate_stats(results):
    if not results:
        return ["0", "0", "0ms", "0ms", "0ms"]
    total = len(results)
    errors = sum(1 for r in results if r['error'])
    latencies = [r['latency'] for r in results]
    avg_lat = statistics.mean(latencies) if latencies else 0
    latencies.sort()
    p95 = latencies[int(total * 0.95)] if total > 0 else 0
    p99 = latencies[int(total * 0.99)] if total > 0 else 0
    return [str(total), str(errors), f"{avg_lat:.2f}ms", f"{p95:.2f}ms", f"{p99:.2f}ms"]

def generate_timeline(start_ts, all_results):
    buckets = {}
    max_second = 0
    for r in all_results:
        rel_sec = int(r['timestamp'] - start_ts)
        if rel_sec < 0: rel_sec = 0
        if rel_sec > max_second: max_second = rel_sec
        if rel_sec not in buckets:
            buckets[rel_sec] = {'total': 0, 'errors': 0, 'avg_lat': 0, 'lat_sum': 0}
        b = buckets[rel_sec]
        b['total'] += 1
        b['lat_sum'] += r['latency']
        if r['error']:
            b['errors'] += 1

    lines = []
    lines.append("| Segundo | Reqs | Erros | Latência | Status Visual |")
    lines.append("|:-------:|:----:|:-----:|:--------:|:--------------|")

    for sec in range(max_second + 1):
        if sec not in buckets:
            continue
        b = buckets[sec]
        avg = b['lat_sum'] / b['total']
        error_rate = (b['errors'] / b['total']) * 100
        
        bar_len = 10
        red_chars = int((error_rate / 100) * bar_len)
        green_chars = bar_len - red_chars
        visual = "🟥" * red_chars + "🟩" * green_chars
        
        status_msg = ""
        if error_rate == 100: status_msg = "**DOWN**"
        elif error_rate > 0: status_msg = "**UNSTABLE**"
        
        lines.append(f"| {sec}s | {b['total']} | {b['errors']} | {avg:.0f}ms | {visual} {status_msg} |")
        
    return "\n".join(lines)

def run():
    wait_for_server()
    
    print(f"🚀 Iniciando Load Test por {DURATION}s ({CONCURRENCY} threads)...")
    print(f"🎯 Target: {TARGET_URL}")
    
    start_ts = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(worker) for _ in range(CONCURRENCY)]
        concurrent.futures.wait(futures)
        
    print("✅ Teste finalizado. Gerando relatório...")
    
    read_stats = calculate_stats(reads_results)
    write_stats = calculate_stats(writes_results)
    all_results = reads_results + writes_results
    timeline_md = generate_timeline(start_ts, all_results)

    report_content = f"""
# 📊 Relatório de Experimento: Sistemas Distribuídos

**Data:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 1. Configurações do Ambiente

| Variável | Valor Configurado |
| :--- | :--- |
"""
    for k, v in ENV_CONFIGS.items():
        report_content += f"| `{k}` | {v} |\n"

    report_content += f"""
## 2. Resultados de Performance

| Tipo | Total Reqs | Qtd Erros | Latência Média | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Escrita (POST)** | {write_stats[0]} | {write_stats[1]} | {write_stats[2]} | {write_stats[3]} | {write_stats[4]} |
| **Leitura (GET)** | {read_stats[0]} | {read_stats[1]} | {read_stats[2]} | {read_stats[3]} | {read_stats[4]} |

## 3. Timeline de Disponibilidade

Este gráfico reflete a visão do cliente sobre a saúde do sistema.

{timeline_md}

---
*Relatório gerado automaticamente pelo LoadTester.*
"""

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(report_content)
    
    print(f"📄 Relatório salvo em: {OUTPUT_FILE}")
    print(report_content)

if __name__ == "__main__":
    run()