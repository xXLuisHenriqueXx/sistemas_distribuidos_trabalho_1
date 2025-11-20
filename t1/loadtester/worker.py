import asyncio
import aiohttp
import random
import time
import datetime

# --- Constantes para a simulação ---

# Status possíveis, baseados no seed.js
STATUSES = ["PENDING", "PAID", "SHIPPED", "CANCELLED"]
# Contagem de usuários, baseada no seed.js
USER_COUNT = 5000
# Intervalo de datas, baseado no seed.js
START_TIMESTAMP = int(datetime.datetime(2020, 1, 1).timestamp())
END_TIMESTAMP = int(datetime.datetime(2025, 1, 1).timestamp())


def generate_random_datetime():
    """Gera um objeto datetime aleatório dentro do intervalo."""
    rand_ts = random.randint(START_TIMESTAMP, END_TIMESTAMP)
    return datetime.datetime.fromtimestamp(rand_ts)


async def worker(
    session: aiohttp.ClientSession,
    wid: int,
    read_boundary: float,
    url: str,
    duration: int,
    db_type: str,            # db_type não é mais usado aqui, mas mantido por consistência
    dataset_size: int,
    start_time: float,
    order_ids_lock: asyncio.Lock,
    order_ids: list,
    read_latencies: list,
    write_latencies: list,
    increment_read_error,
    increment_write_error
):
    """Simula um usuário fazendo requisições."""

    if start_time is None:
        print(f"ERRO: Worker {wid} iniciado antes do start_time ser definido.")
        return

    while time.time() - start_time < duration:
        t0 = time.time()
        op_roll = random.random()
        
        try:
            if op_roll < read_boundary:
                endpoint_url = None
                
                read_op_type = random.randint(1, 4)

                # 1. Buscar por ID
                if read_op_type == 1:
                    oid = None
                    async with order_ids_lock:
                        if order_ids:
                            oid = random.choice(order_ids)
                    if oid:
                        endpoint_url = f"{url}/orders/{oid}"

                # 2. Buscar por User ID
                elif read_op_type == 2:
                    rand_user = random.randint(1, USER_COUNT)
                    endpoint_url = f"{url}/orders/by-user/{rand_user}?limit=20"

                # 3. Buscar por Status
                elif read_op_type == 3:
                    rand_status = random.choice(STATUSES)
                    endpoint_url = f"{url}/orders/by-status/{rand_status}?limit=50"

                # 4. Buscar por Intervalo de Datas
                else: # read_op_type == 4
                    date1 = generate_random_datetime()
                    date2 = generate_random_datetime()
                    from_date = min(date1, date2).isoformat()
                    to_date = max(date1, date2).isoformat()
                    endpoint_url = f"{url}/orders/range?from={from_date}&to={to_date}&limit=100"

                # Executa a requisição GET, se um endpoint válido foi construído
                if endpoint_url:
                    async with session.get(endpoint_url) as resp:
                        await resp.text()
                        resp.raise_for_status()
                    read_latencies.append(time.time() - t0)
                else:
                    await asyncio.sleep(0.01)
                    continue

            # --- Escrita ---
            else:
                # Gera um payload de ordem compatível com o server.js (POST /orders)
                payload = {
                    "user_id": random.randint(1, USER_COUNT),
                    "status": random.choice(STATUSES),
                    "total_value": round(random.uniform(5.0, 2000.0), 2),
                    "created_at": generate_random_datetime().isoformat()
                }

                async with session.post(f"{url}/orders", json=payload) as resp:
                    await resp.text()
                    if resp.status != 201: 
                        raise aiohttp.ClientResponseError(
                            resp.request_info, resp.history,
                            status=resp.status, message=f"Expected 201, got {resp.status}"
                        )
                write_latencies.append(time.time() - t0)

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            # Incrementa o erro correspondente
            if op_roll < read_boundary:
                increment_read_error()
            else:
                increment_write_error()
            # Opcional: Logar o erro específico
            # print(f"Erro no worker {wid}: {type(e).__name__}")
        except Exception as e: # Captura outros erros inesperados
            print(f"ERRO INESPERADO no worker {wid}: {e}")
            # Decide se erros inesperados devem ser contados e como
            if op_roll < read_boundary: increment_read_error()
            else: increment_write_error()


        # Pequena pausa para ceder controle ao event loop
        await asyncio.sleep(0.001)