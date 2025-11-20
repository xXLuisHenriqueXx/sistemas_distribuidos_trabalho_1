import asyncio
import docker
import statistics
import time # Embora não usado diretamente, time pode ser útil para debugging futuro

class ContainerMonitor:
    """Classe para monitorar CPU, memória e rede de um contêiner Docker."""
    def __init__(self, target_name):
        """Inicializa o monitor."""
        try:
            self.client = docker.from_env()
        except Exception as e:
            raise RuntimeError(f"Falha ao conectar ao Docker daemon: {e}") from e
        self.target_name = target_name
        self.container = self._find_container() # Encontra o container na inicialização
        if not self.container:
             raise RuntimeError(f"Contêiner alvo '{self.target_name}' não encontrado.")

        self.cpu_samples = []
        self.mem_samples = []
        self.net_tx_initial = 0
        self.net_rx_initial = 0
        self.net_tx_last = 0
        self.net_rx_last = 0
        self.running = True
        self._get_initial_network_stats() # Pega stats iniciais da rede

    def _find_container(self):
        """Encontra o contêiner alvo pelo nome."""
        try:
            containers = self.client.containers.list()
            for c in containers:
                if self.target_name in c.name:
                    print(f"Monitorando contêiner: {c.name} ({c.short_id})")
                    return c
        except docker.errors.APIError as e:
             print(f"Erro de API do Docker ao listar contêineres: {e}")
        return None

    def _get_initial_network_stats(self):
        """Obtém as estatísticas de rede iniciais para calcular o delta."""
        try:
            stats = self.container.stats(stream=False)
            if "networks" in stats:
                self.net_tx_initial = sum(n.get("tx_bytes", 0) for n in stats["networks"].values())
                self.net_rx_initial = sum(n.get("rx_bytes", 0) for n in stats["networks"].values())
                self.net_tx_last = self.net_tx_initial
                self.net_rx_last = self.net_rx_initial
        except (docker.errors.APIError, KeyError, AttributeError) as e:
             print(f"Aviso: Não foi possível obter estatísticas de rede iniciais: {e}")
             self.net_tx_initial = 0
             self.net_rx_initial = 0
             self.net_tx_last = 0
             self.net_rx_last = 0


    async def collect_metrics(self, interval=1.0):
        """Coleta métricas de CPU, memória e rede em intervalos regulares."""
        print(f"Iniciando coleta de métricas para '{self.target_name}'...")
        prev_cpu_total = 0
        prev_system_cpu = 0

        # Pega os valores iniciais antes do loop
        try:
            initial_stats = self.container.stats(stream=False)
            prev_cpu_total = initial_stats.get("cpu_stats", {}).get("cpu_usage", {}).get("total_usage", 0)
            prev_system_cpu = initial_stats.get("cpu_stats", {}).get("system_cpu_usage", 0)
        except (docker.errors.NotFound, docker.errors.APIError) as e:
            print(f"Erro ao obter estatísticas iniciais: {e}")
            self.running = False # Para a coleta se o container sumir

        while self.running:
            try:
                # Verifica se o container ainda existe
                self.container.reload()
                stats = self.container.stats(stream=False)

                # --- Cálculo de CPU ---
                cpu_stats = stats.get("cpu_stats", {})
                cpu_usage = cpu_stats.get("cpu_usage", {})
                system_cpu_usage = cpu_stats.get("system_cpu_usage") # Pode ser None
                cpu_total = cpu_usage.get("total_usage", 0)

                # system_cpu_usage pode não estar presente em algumas configurações (ex: Docker Desktop no Mac)
                if system_cpu_usage is not None and prev_system_cpu is not None and system_cpu_usage > prev_system_cpu:
                    cpu_delta = cpu_total - prev_cpu_total
                    system_delta = system_cpu_usage - prev_system_cpu

                    if system_delta > 0 and cpu_delta >= 0: # Garante deltas válidos
                        online_cpus = cpu_stats.get("online_cpus", len(cpu_usage.get("percpu_usage", [1])))
                        cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0
                        # Limita a um valor razoável (considerando o número de CPUs)
                        cpu_percent = min(cpu_percent, online_cpus * 100.0)
                        self.cpu_samples.append(cpu_percent)
                # Else: Não calcula CPU se não tiver system_cpu_usage

                prev_cpu_total = cpu_total
                prev_system_cpu = system_cpu_usage

                # --- Cálculo de Memória ---
                mem_stats = stats.get("memory_stats", {})
                # Usa 'usage' - 'cache' para obter memória RSS (mais realista) se disponível
                mem_usage = mem_stats.get("usage", 0)
                mem_cache = mem_stats.get("stats", {}).get("cache", 0)
                actual_mem_usage = mem_usage - mem_cache if mem_usage > mem_cache else mem_usage
                mem_usage_mb = actual_mem_usage / (1024 * 1024)
                self.mem_samples.append(mem_usage_mb)


                # --- Cálculo de Rede ---
                if "networks" in stats:
                    current_tx = sum(n.get("tx_bytes", 0) for n in stats["networks"].values())
                    current_rx = sum(n.get("rx_bytes", 0) for n in stats["networks"].values())
                    self.net_tx_last = current_tx
                    self.net_rx_last = current_rx

            except docker.errors.NotFound:
                print(f"Aviso: Contêiner '{self.target_name}' não encontrado durante a coleta. Parando o monitor.")
                self.running = False
                break # Sai do loop while
            except (docker.errors.APIError, KeyError, AttributeError, TypeError) as e:
                print(f"Erro durante a coleta de métricas: {e}")
                # Continua tentando, pode ser um erro temporário

            await asyncio.sleep(interval)
        print(f"Coleta de métricas para '{self.target_name}' encerrada.")


    def summary(self):
        """Calcula e retorna um resumo das métricas coletadas."""
        # Calcula rede total transmitida/recebida durante o teste
        net_tx_total = (self.net_tx_last - self.net_tx_initial) / (1024 * 1024)
        net_rx_total = (self.net_rx_last - self.net_rx_initial) / (1024 * 1024)

        # Garante valores não negativos para a rede
        net_tx_total = max(0, net_tx_total)
        net_rx_total = max(0, net_rx_total)

        return {
            "cpu_avg": statistics.mean(self.cpu_samples) if self.cpu_samples else 0,
            "cpu_max": max(self.cpu_samples) if self.cpu_samples else 0,
            "mem_avg": statistics.mean(self.mem_samples) if self.mem_samples else 0,
            "mem_max": max(self.mem_samples) if self.mem_samples else 0,
            "net_tx": net_tx_total, # Agora é o total transferido durante o teste
            "net_rx": net_rx_total, # Agora é o total recebido durante o teste
        }
