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

## 🧪 Test Run: 2025-10-24 18:51:43

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
**Total Requests:** 11483 | **Total Errors:** 0 | **Req/Sec:** 184.74

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5712 | 0 | 470.03 | 1257.24 | 1400.97 |
| **Write** | 5771 | 0 | 514.70 | 1268.50 | 1436.96 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.21 | 37.22 |
| **Memory (MB)** | 116.65 | 159.68 |
| **Net TX (MB)** | - | 13.64 |
| **Net RX (MB)** | - | 10.26 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2585 | 540.16 | N/A | 594.80 | 29.59 | 136.97 |
| 33 | 3081 | 501.06 | N/A | 551.72 | 31.62 | 122.72 |
| 48 | 3245 | 478.52 | N/A | 521.07 | 32.28 | 118.46 |

---

## 🧪 Test Run: 2025-10-24 18:53:44

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
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
**Total Requests:** 11500 | **Total Errors:** 0 | **Req/Sec:** 184.94

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5759 | 0 | 475.77 | 1291.20 | 1392.91 |
| **Write** | 5741 | 0 | 507.02 | 1292.93 | 1395.82 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.58 | 37.90 |
| **Memory (MB)** | 107.24 | 149.97 |
| **Net TX (MB)** | - | 13.65 |
| **Net RX (MB)** | - | 10.28 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2518 | 553.35 | N/A | 610.56 | 30.45 | 127.48 |
| 33 | 3046 | 514.79 | N/A | 558.86 | 31.91 | 113.53 |
| 48 | 3404 | 476.94 | N/A | 516.08 | 32.60 | 109.19 |

---

## 🧪 Test Run: 2025-10-24 18:58:08

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 10887 | **Total Errors:** 0 | **Req/Sec:** 174.99

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5464 | 0 | 505.73 | 1282.33 | 1455.16 |
| **Write** | 5423 | 0 | 535.21 | 1296.31 | 1489.46 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.44 | 43.27 |
| **Memory (MB)** | 98.47 | 110.45 |
| **Net TX (MB)** | - | 12.00 |
| **Net RX (MB)** | - | 9.04 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2325 | 595.76 | N/A | 678.61 | 31.29 | 100.07 |
| 33 | 2860 | 558.63 | N/A | 596.34 | 32.22 | 98.24 |
| 48 | 3088 | 522.70 | N/A | 552.29 | 32.44 | 98.28 |

---

