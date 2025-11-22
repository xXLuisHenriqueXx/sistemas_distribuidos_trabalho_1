
# Relatório de Experimento: Sistemas Distribuídos

**Data:** 2025-11-22 16:28:56

## 1. Configurações do Ambiente

| Variável | Valor Configurado |
| :--- | :--- |
| `READ_PREFERENCE` | secondaryPreferred |
| `WRITE_CONCERN` | 1 |
| `CHAOS_FAILURE_CHANCE` | 1.0 |
| `DATASET_SIZE` | 10000 |
| `COMPLEX_DOC_RATIO` | 0.6 |

## 2. Resultados de Performance

| Tipo | Total Reqs | Qtd Erros | Latência Média | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Escrita (POST)** | 872 | 150 | 383.67ms | 2004.37ms | 2006.77ms |
| **Leitura (GET)** | 3366 | 0 | 21.14ms | 54.70ms | 77.43ms |

## 3. Timeline de Disponibilidade

Este gráfico reflete a visão do cliente sobre a saúde do sistema.

| Segundo | Reqs | Erros | Latência | Status Visual |
|:-------:|:----:|:-----:|:--------:|:--------------|
| 0s | 312 | 0 | 21ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 1s | 306 | 0 | 21ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 2s | 299 | 0 | 23ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 3s | 274 | 0 | 24ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 4s | 316 | 0 | 21ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 5s | 42 | 10 | 489ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 7s | 46 | 10 | 443ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 9s | 46 | 10 | 442ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 11s | 36 | 10 | 563ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 13s | 42 | 10 | 484ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 15s | 44 | 1 | 414ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 17s | 154 | 0 | 35ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 18s | 297 | 0 | 22ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 19s | 254 | 10 | 95ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 21s | 51 | 9 | 360ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 22s | 2 | 1 | 1006ms | 🟥🟥🟥🟥🟥🟩🟩🟩🟩🟩 **UNSTABLE** |
| 23s | 31 | 7 | 459ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 24s | 21 | 3 | 293ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 25s | 19 | 6 | 641ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 26s | 29 | 4 | 284ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 27s | 22 | 4 | 373ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 28s | 25 | 4 | 467ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 29s | 15 | 0 | 89ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 30s | 184 | 0 | 33ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 31s | 328 | 0 | 19ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 32s | 319 | 0 | 19ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 33s | 281 | 0 | 24ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 34s | 233 | 11 | 109ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 36s | 40 | 8 | 407ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 37s | 21 | 2 | 199ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 38s | 25 | 4 | 327ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 39s | 19 | 6 | 638ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 40s | 22 | 4 | 371ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 41s | 16 | 6 | 756ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 42s | 6 | 2 | 674ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 43s | 58 | 8 | 283ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 44s | 2 | 0 | 981ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 45s | 1 | 0 | 8ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |

---
*Relatório gerado automaticamente pelo LoadTester.*
