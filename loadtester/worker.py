import asyncio
import aiohttp
import random
import time
import random
import datetime
import time

# Se LOREM_WORDS for usado apenas aqui, mova-o para cá
LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
    "adipcing", "elit", "sed", "do", "eiusmod", "tempor",
    "incididunt", "ut", "labore", "et", "dolore", "magna",
    "culpa", "qui", "officia", "deserunt", "mollit", "anim",
    "id", "est", "laborum"
]

def generate_lorem_ipsum(max_words=100):
    """Gera texto Lorem Ipsum com um número aleatório de palavras."""
    num_words = random.randint(max_words // 2, max_words) # Gera um tamanho mais consistente
    content = " ".join(random.choices(LOREM_WORDS, k=num_words))
    return content.capitalize() + "."

async def worker(
    session: aiohttp.ClientSession,
    wid: int,
    read_boundary: float,
    url: str,
    duration: int,
    db_type: str,
    dataset_size: int,
    start_time: float,
    post_ids_lock: asyncio.Lock,
    post_ids: list,
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
                pid = None
                async with post_ids_lock:
                    if post_ids:
                        pid = random.choice(post_ids)

                if pid:
                    async with session.get(f"{url}/posts/{pid}") as resp:
                        await resp.text() # Consome a resposta
                        resp.raise_for_status() # Verifica erro HTTP
                    read_latencies.append(time.time() - t0)
                else:
                    await asyncio.sleep(0.05)
                    continue

            # --- Escrita ---
            else:
                content_payload = generate_lorem_ipsum(max_words=50)
                payload = {}
                title = f"T_{wid}_{t0:.4f}" # Título único simples
                if db_type == "postgres":
                    payload = {
                        "user_id": random.randint(1, 1000),
                        "title": title,
                        "content": content_payload
                    }
                else:  # mongo
                    username = f"U_{wid}_{t0:.4f}"  # Username único simples

                    # Gerar data aleatória entre 2022-01-01 e 2025-01-01
                    start_date = datetime.date(2022, 1, 1)
                    end_date = datetime.date(2025, 1, 1)
                    delta_days = (end_date - start_date).days
                    random_days = random.randint(0, delta_days)
                    created_at = start_date + datetime.timedelta(days=random_days)

                    payload = {
                        "author": {
                            "user_id": random.randint(1, 1000),
                            "username": username
                        },
                        "title": title,
                        "content": content_payload,
                        "created_at": created_at.isoformat()  # formato YYYY-MM-DD
                    }


                async with session.post(f"{url}/posts", json=payload) as resp:
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
