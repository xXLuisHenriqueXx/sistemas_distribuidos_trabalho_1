## 🧪 Test Run: 2025-10-24 19:53:53

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
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
**Total Requests:** 24196 | **Total Errors:** 0 | **Req/Sec:** 390.18

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 12112 | 0 | 225.64 | 1098.52 | 1167.60 |
| **Write** | 12084 | 0 | 232.08 | 1098.68 | 1169.53 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 29.09 | 34.14 |
| **Memory (MB)** | 94.03 | 97.31 |
| **Net TX (MB)** | - | 66.33 |
| **Net RX (MB)** | - | 45.31 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 5677 | 252.91 | 267.88 | 26.89 | 88.81 |
| 33 | 6480 | 238.87 | 250.22 | 28.24 | 92.63 |
| 48 | 7610 | 222.35 | 228.06 | 29.04 | 93.66 |

---

## 🧪 Test Run: 2025-10-24 19:55:57

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
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
**Total Requests:** 19576 | **Total Errors:** 0 | **Req/Sec:** 315.63

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 9838 | 0 | 294.42 | 1130.65 | 1210.44 |
| **Write** | 9738 | 0 | 271.65 | 1113.58 | 1198.72 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 29.58 | 33.85 |
| **Memory (MB)** | 82.84 | 85.74 |
| **Net TX (MB)** | - | 52.98 |
| **Net RX (MB)** | - | 36.92 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 4366 | 340.13 | 332.88 | 27.55 | 77.61 |
| 33 | 5137 | 320.67 | 305.09 | 28.84 | 81.00 |
| 48 | 6330 | 291.01 | 271.01 | 29.60 | 82.21 |

---

## 🧪 Test Run: 2025-10-24 20:03:24

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
**Total Requests:** 8678 | **Total Errors:** 0 | **Req/Sec:** 137.21

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 4365 | 0 | 635.92 | 1402.71 | 1531.39 |
| **Write** | 4313 | 0 | 691.27 | 1418.84 | 1645.36 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 35.02 | 39.54 |
| **Memory (MB)** | 100.15 | 145.91 |
| **Net TX (MB)** | - | 30.80 |
| **Net RX (MB)** | - | 23.11 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1902 | 717.09 | 825.31 | 32.31 | 111.85 |
| 33 | 2271 | 681.83 | 749.96 | 34.37 | 103.14 |
| 48 | 2458 | 639.16 | 704.00 | 34.62 | 101.01 |
| 63 | 2047 | 635.92 | 691.27 | 35.02 | 100.15 |

---

## 🧪 Test Run: 2025-10-24 20:05:19

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
**Total Requests:** 8675 | **Total Errors:** 0 | **Req/Sec:** 137.17

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 4238 | 0 | 626.45 | 1408.68 | 1588.07 |
| **Write** | 4437 | 0 | 682.74 | 1415.56 | 1664.95 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 34.49 | 39.95 |
| **Memory (MB)** | 100.84 | 146.98 |
| **Net TX (MB)** | - | 29.95 |
| **Net RX (MB)** | - | 22.46 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1934 | 695.14 | 813.93 | 31.19 | 112.18 |
| 33 | 2360 | 651.27 | 738.52 | 33.97 | 104.36 |
| 48 | 2445 | 626.24 | 692.80 | 34.56 | 101.91 |
| 63 | 1936 | 626.45 | 682.74 | 34.49 | 100.84 |

---

## 🧪 Test Run: 2025-10-24 20:08:58

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
**Total Requests:** 8635 | **Total Errors:** 0 | **Req/Sec:** 136.51

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 4324 | 0 | 639.45 | 1409.88 | 1597.67 |
| **Write** | 4311 | 0 | 696.00 | 1443.72 | 1616.66 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 35.31 | 41.66 |
| **Memory (MB)** | 97.79 | 149.54 |
| **Net TX (MB)** | - | 31.03 |
| **Net RX (MB)** | - | 23.29 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1865 | 726.60 | 835.88 | 31.48 | 102.18 |
| 33 | 2319 | 674.31 | 753.87 | 34.94 | 98.67 |
| 48 | 2467 | 634.00 | 703.35 | 35.41 | 98.03 |
| 63 | 1984 | 639.45 | 696.00 | 35.31 | 97.79 |

---

## 🧪 Test Run: 2025-10-24 20:12:33

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 13027 | **Total Errors:** 0 | **Req/Sec:** 209.43

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 13027 | 0 | 435.32 | 1245.39 | 1349.59 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.18 | 35.99 |
| **Memory (MB)** | 99.61 | 147.55 |
| **Net TX (MB)** | - | 10.97 |
| **Net RX (MB)** | - | 7.16 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2688 | 0.00 | 551.08 | 28.52 | 115.10 |
| 33 | 3424 | 0.00 | 489.28 | 30.65 | 104.24 |
| 48 | 3846 | 0.00 | 448.44 | 31.55 | 101.07 |

---

## 🧪 Test Run: 2025-10-24 20:14:38

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 11960 | **Total Errors:** 0 | **Req/Sec:** 189.03

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 11960 | 0 | 478.73 | 1270.41 | 1417.56 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.41 | 37.86 |
| **Memory (MB)** | 105.03 | 150.08 |
| **Net TX (MB)** | - | 10.50 |
| **Net RX (MB)** | - | 6.89 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2523 | 0.00 | 582.89 | 30.03 | 120.44 |
| 33 | 3101 | 0.00 | 529.88 | 31.20 | 109.69 |
| 48 | 3665 | 0.00 | 479.52 | 32.52 | 106.75 |
| 63 | 2671 | 0.00 | 478.73 | 32.41 | 105.03 |

---

## 🧪 Test Run: 2025-10-24 20:22:18

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 13144 | **Total Errors:** 0 | **Req/Sec:** 211.37

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 13144 | 0 | 429.90 | 1238.75 | 1380.34 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.47 | 36.79 |
| **Memory (MB)** | 105.86 | 158.72 |
| **Net TX (MB)** | - | 11.09 |
| **Net RX (MB)** | - | 7.23 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2566 | 0.00 | 570.62 | 28.30 | 116.96 |
| 33 | 3658 | 0.00 | 478.98 | 31.54 | 108.83 |
| 48 | 3897 | 0.00 | 439.13 | 31.94 | 106.76 |

---

## 🧪 Test Run: 2025-10-24 20:24:59

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 13054 | **Total Errors:** 0 | **Req/Sec:** 206.39

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 13054 | 0 | 434.73 | 1254.19 | 1371.86 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 31.76 | 36.94 |
| **Memory (MB)** | 98.34 | 146.36 |
| **Net TX (MB)** | - | 11.30 |
| **Net RX (MB)** | - | 7.37 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2720 | 0.00 | 543.10 | 28.73 | 115.81 |
| 33 | 3463 | 0.00 | 482.63 | 30.77 | 103.87 |
| 48 | 3936 | 0.00 | 439.58 | 31.81 | 100.37 |
| 63 | 2935 | 0.00 | 434.73 | 31.76 | 98.34 |

---

