import asyncio
import aiohttp
import os
import random
import statistics
import time
import docker
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("TARGET_URL", "http://app:3000")
DURATION = int(os.getenv("DURATION", "30"))
CONCURRENCY = int(os.getenv("CONCURRENCY", "100"))
READ_RATIO = float(os.getenv("READ_RATIO", "0.5"))
DATASET_SIZE = int(os.getenv("DATASET_SIZE", "50000"))
MONITOR_TARGET = os.getenv("MONITOR_TARGET", "app")
REPORT_INTERVAL = int(os.getenv("REPORT_INTERVAL", "10")) 

latencies = []
errors = 0
start_time = None

# ---------- Docker metrics monitor ----------
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
            stats = container.stats(stream=False)
            cpu_total = stats["cpu_stats"]["cpu_usage"]["total_usage"]
            system_cpu = stats["cpu_stats"]["system_cpu_usage"]
            online_cpus = stats["cpu_stats"].get("online_cpus", 1)

            # CPU %
            if prev_cpu is not None:
                cpu_delta = cpu_total - prev_cpu
                system_delta = system_cpu - prev_system
                cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0 if system_delta > 0 else 0
                self.cpu_samples.append(cpu_percent)

            prev_cpu = cpu_total
            prev_system = system_cpu

            # Memory (MB)
            mem_usage = stats["memory_stats"]["usage"] / (1024 * 1024)
            self.mem_samples.append(mem_usage)

            # Network
            if "networks" in stats:
                tx = sum(n["tx_bytes"] for n in stats["networks"].values())
                rx = sum(n["rx_bytes"] for n in stats["networks"].values())
                self.net_tx = tx
                self.net_rx = rx

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

# ---------- Load test logic ----------
async def worker(session, wid):
    global errors
    while time.time() - start_time < DURATION:
        t0 = time.time()
        try:
            if random.random() < READ_RATIO:
                pid = random.randint(1, DATASET_SIZE)
                async with session.get(f"{URL}/posts/{pid}") as resp:
                    await resp.text()
            else:
                payload = {
                    "user_id": random.randint(1, 1000),
                    "title": f"Title {random.randint(1, 1000000)}",
                    "content": "Lorem ipsum dolor sit amet."
                }
                async with session.post(f"{URL}/posts", json=payload) as resp:
                    await resp.text()
            latencies.append(time.time() - t0)
        except Exception:
            errors += 1

# ---------- Periodic reporter ----------
async def periodic_reporter(monitor):
    last_count = 0
    while time.time() - start_time < DURATION:
        await asyncio.sleep(REPORT_INTERVAL)
        count = len(latencies)
        delta = count - last_count
        last_count = count

        duration = time.time() - start_time
        summary = monitor.summary()
        avg = statistics.mean(latencies) * 1000 if latencies else 0
        p95 = statistics.quantiles(latencies, n=100)[94] * 1000 if len(latencies) > 100 else 0
        p99 = statistics.quantiles(latencies, n=100)[98] * 1000 if len(latencies) > 100 else 0

        print(f"\n[+{int(duration)}s] Progress report:")
        print(f"  Total requests: {count} (+{delta} in last {REPORT_INTERVAL}s)")
        print(f"  Errors: {errors}")
        print(f"  Avg latency: {avg:.2f} ms | p95: {p95:.2f} | p99: {p99:.2f}")
        print(f"  CPU avg/max: {summary['cpu_avg']:.2f}% / {summary['cpu_max']:.2f}%")
        print(f"  Mem avg/max: {summary['mem_avg']:.2f} MB / {summary['mem_max']:.2f} MB")
        print(f"  Net TX/RX: {summary['net_tx']:.2f} MB / {summary['net_rx']:.2f} MB")
        print("--------------------------------------------------")

# ---------- Main ----------
async def main():
    global start_time
    print(f"Starting load test: {CONCURRENCY} clients, {DURATION}s, reads={READ_RATIO}, writes={1 - READ_RATIO}")

    monitor = ContainerMonitor(MONITOR_TARGET)
    monitor_task = asyncio.create_task(monitor.collect_metrics())
    reporter_task = asyncio.create_task(periodic_reporter(monitor))

    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = [asyncio.create_task(worker(session, i)) for i in range(CONCURRENCY)]
        await asyncio.gather(*tasks)

    monitor.running = False
    await asyncio.sleep(1)

    reporter_task.cancel()

    duration = time.time() - start_time
    summary = monitor.summary()

    if latencies:
        avg = statistics.mean(latencies)
        p95 = statistics.quantiles(latencies, n=100)[94]
        p99 = statistics.quantiles(latencies, n=100)[98]
    else:
        avg = p95 = p99 = 0

    print("\n=== FINAL RESULTS ===")
    print(f"Total requests: {len(latencies)}")
    print(f"Errors: {errors}")
    print(f"Duration: {duration:.2f}s")
    print(f"Avg latency: {avg*1000:.2f} ms")
    print(f"p95: {p95*1000:.2f} ms | p99: {p99*1000:.2f} ms")
    print(f"Req/sec: {len(latencies)/duration:.2f}")
    print("----------------")
    print(f"CPU avg/max: {summary['cpu_avg']:.2f}% / {summary['cpu_max']:.2f}%")
    print(f"Memory avg/max: {summary['mem_avg']:.2f} MB / {summary['mem_max']:.2f} MB")
    print(f"Network TX/RX: {summary['net_tx']:.2f} MB / {summary['net_rx']:.2f} MB")
    print("================")

if __name__ == "__main__":
    asyncio.run(main())
