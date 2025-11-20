
# 📊 Relatório de Experimento: Sistemas Distribuídos

**Data:** 2025-11-20 17:15:46

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
| **Escrita (POST)** | 1102 | 128 | 276.36ms | 2012.31ms | 2013.48ms |
| **Leitura (GET)** | 4635 | 0 | 17.64ms | 36.17ms | 61.96ms |

## 3. Timeline de Disponibilidade

Este gráfico reflete a visão do cliente sobre a saúde do sistema.

| Segundo | Reqs | Erros | Latência | Status Visual |
|:-------:|:----:|:-----:|:--------:|:--------------|
| 0s | 311 | 0 | 21ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 1s | 344 | 0 | 17ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 2s | 318 | 0 | 21ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 3s | 352 | 0 | 17ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 4s | 306 | 6 | 60ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 5s | 30 | 4 | 279ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 6s | 8 | 2 | 512ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 7s | 31 | 8 | 527ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 8s | 2 | 0 | 11ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 9s | 89 | 10 | 236ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 11s | 44 | 10 | 466ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 13s | 66 | 1 | 240ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 14s | 1 | 0 | 1214ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 15s | 264 | 0 | 19ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 16s | 343 | 0 | 18ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 17s | 377 | 0 | 15ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 18s | 373 | 0 | 16ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 19s | 358 | 7 | 49ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 20s | 15 | 4 | 545ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 21s | 16 | 3 | 386ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 22s | 52 | 7 | 281ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 23s | 6 | 2 | 678ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 24s | 51 | 8 | 325ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 25s | 4 | 0 | 11ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 26s | 47 | 10 | 437ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 28s | 67 | 6 | 305ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 30s | 131 | 0 | 29ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 31s | 373 | 0 | 15ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 32s | 378 | 0 | 15ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 33s | 377 | 0 | 15ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |
| 34s | 349 | 7 | 57ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 35s | 9 | 3 | 677ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 36s | 9 | 1 | 234ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 37s | 45 | 9 | 412ms | 🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 38s | 3 | 1 | 678ms | 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 39s | 75 | 9 | 252ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 41s | 64 | 10 | 324ms | 🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩 **UNSTABLE** |
| 43s | 49 | 0 | 317ms | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩  |

---
*Relatório gerado automaticamente pelo LoadTester.*
