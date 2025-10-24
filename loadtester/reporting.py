import statistics
import datetime

def calculate_stats(lat_list):
    """Calcula estatísticas (avg, p95, p99) para uma lista de latências."""
    if not lat_list:
        return {'avg_ms': 0, 'p95_ms': 0, 'p99_ms': 0, 'count': 0}

    count = len(lat_list)
    avg = statistics.mean(lat_list)
    p95 = avg # Valor padrão
    p99 = avg # Valor padrão

    # Calcula percentis de forma mais robusta se houver dados suficientes
    if count > 10: # Usar um limiar menor para ter alguma estimativa
        try:
             # Ordena a lista para pegar percentis manualmente
            sorted_lats = sorted(lat_list)
            p95_index = min(int(count * 0.95), count - 1)
            p99_index = min(int(count * 0.99), count - 1)
            # Garante que os índices sejam válidos
            p95_index = max(0, p95_index)
            p99_index = max(0, p99_index)
            p95 = sorted_lats[p95_index]
            p99 = sorted_lats[p99_index]
        except IndexError:
             # Fallback para a média se algo der errado (improvável com as verificações)
             p95 = avg
             p99 = avg
        except Exception as e: # Captura outros erros inesperados
            print(f"Erro inesperado ao calcular percentis: {e}")
            p95 = avg
            p99 = avg


    return {
        'avg_ms': avg * 1000,
        'p95_ms': p95 * 1000,
        'p99_ms': p99 * 1000,
        'count': count
    }

def append_results_to_markdown(config, results, summary, periodic_data, filename="test_results.md"):
    """Anexa os resultados formatados de um teste a um arquivo markdown."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"## 🧪 Test Run: {timestamp}\n\n")

            # --- Seção de Configuração ---
            f.write("### ⚙️ Configuration\n")
            f.write("| Parameter | Value |\n")
            f.write("| :--- | :--- |\n")
            # Adiciona os parâmetros de CPU/Memória do DB se disponíveis
            db_cpus = config.get("DB_CPUS", "N/A")
            db_mem = config.get("DB_MEM", "N/A")
            for key, val in config.items():
                 # Evita duplicar DB_CPUS/DB_MEM se já estiverem no dict principal
                 if key not in ["DB_CPUS", "DB_MEM"]:
                    f.write(f"| **{key}** | {val} |\n")
            # Adiciona DB_CPUS e DB_MEM explicitamente se não estiverem já lá
            if "DB_CPUS" not in config: f.write(f"| **DB_CPUS** | {db_cpus} |\n")
            if "DB_MEM" not in config: f.write(f"| **DB_MEM** | {db_mem} |\n")

            f.write("\n")


            # --- Seção de Resultados Finais ---
            f.write("### 📊 Performance Results (Final)\n")
            f.write(f"**Total Requests:** {results.get('total_requests', 0)} | ")
            f.write(f"**Total Errors:** {results.get('total_errors', 0)} | ")
            f.write(f"**Req/Sec:** {results.get('req_per_sec', 0):.2f}\n\n")

            f.write("| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            f.write(f"| **Read (Primary)** | {results.get('read_reqs', 0)} | {results.get('errors_read', 0)} | {results.get('read_avg_ms', 0):.2f} | {results.get('read_p95_ms', 0):.2f} | {results.get('read_p99_ms', 0):.2f} |\n")
            # Só mostra a linha de Read Secondary se estiver habilitado na config
            if config.get('ENABLE_SECONDARY_READS', False):
                f.write(f"| **Read (Secondary)** | {results.get('secondary_reqs', 0)} | {results.get('errors_secondary', 0)} | {results.get('secondary_avg_ms', 0):.2f} | {results.get('secondary_p95_ms', 0):.2f} | {results.get('secondary_p99_ms', 0):.2f} |\n")
            f.write(f"| **Write** | {results.get('write_reqs', 0)} | {results.get('errors_write', 0)} | {results.get('write_avg_ms', 0):.2f} | {results.get('write_p95_ms', 0):.2f} | {results.get('write_p99_ms', 0):.2f} |\n")
            f.write("\n")

            # --- Seção de Uso de Recursos ---
            monitor_target = config.get('MONITOR_TARGET', 'app')
            f.write(f"### 💻 Resource Usage ({monitor_target} - Final)\n")
            f.write("| Resource | Avg | Max |\n")
            f.write("| :--- | :--- | :--- |\n")
            f.write(f"| **CPU (%)** | {summary.get('cpu_avg', 0):.2f} | {summary.get('cpu_max', 0):.2f} |\n")
            f.write(f"| **Memory (MB)** | {summary.get('mem_avg', 0):.2f} | {summary.get('mem_max', 0):.2f} |\n")
            # Mostra TX/RX como Total
            f.write(f"| **Net TX (MB)** | - | {summary.get('net_tx', 0):.2f} |\n")
            f.write(f"| **Net RX (MB)** | - | {summary.get('net_rx', 0):.2f} |\n")
            f.write("\n")

            # --- Seção de Log Periódico ---
            f.write("### 📈 Periodic Report Log\n")
            # Tabela periódica NÃO inclui p99 para evitar ficar muito larga
            f.write("| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")

            if not periodic_data:
                f.write("| N/A | N/A | N/A | N/A | N/A | N/A | N/A |\n")
            else:
                for report in periodic_data:
                    # Garante que todos os campos esperados existam no dicionário 'report'
                    time_s = report.get('time_s', 'N/A')
                    new_reqs = report.get('new_reqs', 'N/A')
                    read_avg = report.get('read_avg_ms', 0)
                    write_avg = report.get('write_avg_ms', 0)
                    cpu_avg = report.get('cpu_avg_pct', 0)
                    mem_avg = report.get('mem_avg_mb', 0)

                    # Formata Sec.Read Avg condicionalmente
                    sec_avg_val = report.get('secondary_avg_ms', 0)
                    sec_avg = f"{sec_avg_val:.2f}" if config.get('ENABLE_SECONDARY_READS', False) else "N/A"

                    f.write(f"| {time_s} | {new_reqs} | {read_avg:.2f} | {sec_avg} | {write_avg:.2f} | {cpu_avg:.2f} | {mem_avg:.2f} |\n")

            f.write("\n---\n\n") # Separador entre testes

        print(f"\n✅ Resultados anexados em: {filename}")
    except IOError as e:
        print(f"❌ Falha de I/O ao salvar resultados no arquivo '{filename}': {e}")
    except Exception as e:
        print(f"❌ Falha inesperada ao salvar resultados no arquivo: {e}")
