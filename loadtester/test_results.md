## 🧪 Test Run: 2025-10-24 18:34:52

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 10464 | **Total Errors:** 0 | **Req/Sec:** 165.39

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5227 | 0 | 526.73 | 1355.72 | 1481.33 |
| **Write** | 5237 | 0 | 560.87 | 1339.51 | 1478.79 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.51 | 38.72 |
| **Memory (MB)** | 94.53 | 101.55 |
| **Net TX (MB)** | - | 12.98 |
| **Net RX (MB)** | - | 9.67 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2281 | 605.92 | N/A | 677.94 | 30.47 | 92.78 |
| 33 | 2813 | 556.01 | N/A | 617.63 | 32.03 | 93.51 |
| 48 | 3135 | 521.63 | N/A | 563.44 | 32.86 | 94.13 |
| 63 | 2235 | 526.73 | N/A | 560.87 | 32.51 | 94.53 |

---

