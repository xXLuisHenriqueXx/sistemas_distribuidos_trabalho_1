import asyncio
import aiohttp
import os
import random
import statistics
import time
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("TARGET_URL", "http://app:3000")
DURATION = int(os.getenv("DURATION", "30"))
CONCURRENCY = int(os.getenv("CONCURRENCY", "100"))
READ_RATIO = float(os.getenv("READ_RATIO", "0.5"))
DATASET_SIZE = int(os.getenv("DATASET_SIZE", "50000"))

latencies = []
errors = 0
start_time = None

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

async def main():
    global start_time
    print(f"Starting load test: {CONCURRENCY} clients, {DURATION}s, reads={READ_RATIO}, writes={1 - READ_RATIO}")
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = [asyncio.create_task(worker(session, i)) for i in range(CONCURRENCY)]
        await asyncio.gather(*tasks)

    duration = time.time() - start_time
    if latencies:
        avg = statistics.mean(latencies)
        p95 = statistics.quantiles(latencies, n=100)[94]
        p99 = statistics.quantiles(latencies, n=100)[98]
    else:
        avg = p95 = p99 = 0

    print("\n=== RESULTS ===")
    print(f"Total requests: {len(latencies)}")
    print(f"Errors: {errors}")
    print(f"Duration: {duration:.2f}s")
    print(f"Avg latency: {avg*1000:.2f} ms")
    print(f"p95: {p95*1000:.2f} ms | p99: {p99*1000:.2f} ms")
    print(f"Req/sec: {len(latencies)/duration:.2f}")
    print("================")

if __name__ == "__main__":
    asyncio.run(main())
