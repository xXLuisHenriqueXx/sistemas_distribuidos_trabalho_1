# Relatório de testes realizados

Comentar aqui a metodologia
Para cada par de teste (ou seja, mongo e postgres), comentar o que foi observado e porque acontece

---

## 🧪 Test Run: 2025-10-24 17:01:18

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | false |
| **ENABLE_SECONDARY_READS** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 10456 | **Total Errors:** 0 | **Req/Sec:** 170.94

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5256 | 0 | 548.34 | 1346.52 | 1449.87 |
| **Write** | 5200 | 0 | 572.14 | 1341.71 | 1471.46 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.62 | 38.80 |
| **Memory (MB)** | 102.63 | 143.02 |
| **Net TX (MB)** | - | 36.06 |
| **Net RX (MB)** | - | 8.20 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 2163 | 649.40 | N/A | 701.33 | 34.62 | 122.12 |
| 31 | 2614 | 613.60 | N/A | 635.69 | 34.04 | 108.46 |
| 46 | 2958 | 565.80 | N/A | 589.35 | 33.87 | 104.64 |

---

## 🧪 Test Run: 2025-10-24 17:16:38

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | false |
| **ENABLE_SECONDARY_READS** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 32009 | **Total Errors:** 0 | **Req/Sec:** 524.03

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 16092 | 0 | 177.66 | 1057.46 | 1170.67 |
| **Write** | 15917 | 0 | 184.48 | 1060.39 | 1151.52 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.31 | 32.34 |
| **Memory (MB)** | 85.56 | 87.62 |
| **Net TX (MB)** | - | 42.60 |
| **Net RX (MB)** | - | 19.96 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 6966 | 204.19 | N/A | 216.31 | 29.16 | 81.72 |
| 31 | 8367 | 187.69 | N/A | 198.29 | 28.55 | 84.37 |
| 46 | 9111 | 176.88 | N/A | 185.46 | 28.62 | 85.22 |

---

## 🧪 Test Run: 2025-10-24 17:19:16

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 10313 | **Total Errors:** 0 | **Req/Sec:** 165.55

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5229 | 0 | 559.40 | 1346.23 | 1520.13 |
| **Write** | 5084 | 0 | 596.43 | 1345.96 | 1535.91 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.01 | 39.51 |
| **Memory (MB)** | 100.08 | 144.22 |
| **Net TX (MB)** | - | 36.24 |
| **Net RX (MB)** | - | 8.34 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 2084 | 670.65 | N/A | 720.53 | 34.79 | 105.99 |
| 31 | 2629 | 611.34 | N/A | 659.80 | 33.95 | 101.72 |
| 46 | 2870 | 567.42 | N/A | 609.50 | 33.24 | 100.57 |
| 61 | 2730 | 559.40 | N/A | 596.43 | 33.01 | 100.08 |

---

## 🧪 Test Run: 2025-10-24 17:21:20

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 30255 | **Total Errors:** 0 | **Req/Sec:** 495.45

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 15142 | 0 | 190.09 | 1068.01 | 1181.76 |
| **Write** | 15113 | 0 | 191.97 | 1063.14 | 1183.05 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.10 | 32.91 |
| **Memory (MB)** | 84.83 | 88.37 |
| **Net TX (MB)** | - | 41.23 |
| **Net RX (MB)** | - | 18.84 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 5881 | 248.44 | N/A | 248.05 | 29.48 | 78.42 |
| 31 | 7698 | 218.65 | N/A | 216.56 | 28.25 | 82.59 |
| 46 | 9015 | 195.90 | N/A | 196.10 | 28.21 | 83.97 |

---

## 🧪 Test Run: 2025-10-24 17:23:41

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 40% Read_ID, 10% Read_User, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 9722 | **Total Errors:** 1027 | **Req/Sec:** 155.96

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 4239 | 0 | 551.12 | 1359.01 | 1517.70 |
| **Read (Secondary)** | 0 | 1027 | 0.00 | 0.00 | 0.00 |
| **Write** | 5483 | 0 | 594.51 | 1368.81 | 1537.79 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 32.92 | 37.44 |
| **Memory (MB)** | 103.37 | 146.07 |
| **Net TX (MB)** | - | 35.95 |
| **Net RX (MB)** | - | 7.86 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 2049 | 645.79 | 0.00 | 706.75 | 34.10 | 123.13 |
| 31 | 2366 | 611.38 | 0.00 | 670.30 | 33.36 | 109.40 |
| 46 | 2746 | 565.69 | 0.00 | 615.22 | 33.06 | 105.58 |
| 61 | 2561 | 551.12 | 0.00 | 594.51 | 32.92 | 103.37 |

---

## 🧪 Test Run: 2025-10-24 17:25:31

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 40% Read_ID, 10% Read_User, 50% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 27514 | **Total Errors:** 3131 | **Req/Sec:** 449.11

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 12217 | 0 | 200.11 | 1070.39 | 1179.34 |
| **Read (Secondary)** | 0 | 3131 | 0.00 | 0.00 | 0.00 |
| **Write** | 15297 | 0 | 211.52 | 1078.32 | 1191.18 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.24 | 32.58 |
| **Memory (MB)** | 82.10 | 85.27 |
| **Net TX (MB)** | - | 40.39 |
| **Net RX (MB)** | - | 17.27 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 5703 | 242.89 | 0.00 | 260.62 | 28.87 | 76.46 |
| 31 | 6946 | 216.89 | 0.00 | 239.10 | 28.04 | 80.17 |
| 46 | 7886 | 204.39 | 0.00 | 216.69 | 28.30 | 81.46 |
| 61 | 6979 | 200.11 | 0.00 | 211.52 | 28.24 | 82.10 |

---

## 🧪 Test Run: 2025-10-24 17:27:48

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 10% Read_ID, 10% Read_User, 80% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 9670 | **Total Errors:** 1109 | **Req/Sec:** 157.86

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 1122 | 0 | 529.92 | 1371.64 | 1587.60 |
| **Read (Secondary)** | 0 | 1109 | 0.00 | 0.00 | 0.00 |
| **Write** | 8548 | 0 | 576.77 | 1361.69 | 1519.05 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.33 | 38.63 |
| **Memory (MB)** | 99.96 | 146.25 |
| **Net TX (MB)** | - | 34.48 |
| **Net RX (MB)** | - | 6.32 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 1926 | 685.80 | 0.00 | 734.23 | 34.01 | 106.46 |
| 31 | 2502 | 592.47 | 0.00 | 643.76 | 33.60 | 101.67 |
| 46 | 2774 | 546.65 | 0.00 | 590.39 | 33.56 | 100.40 |
| 61 | 2468 | 529.92 | 0.00 | 576.77 | 33.33 | 99.96 |

---

## 🧪 Test Run: 2025-10-24 17:30:03

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 10% Read_ID, 10% Read_User, 80% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 26889 | **Total Errors:** 3142 | **Req/Sec:** 439.50

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 3050 | 0 | 214.16 | 1086.64 | 1171.16 |
| **Read (Secondary)** | 0 | 3142 | 0.00 | 0.00 | 0.00 |
| **Write** | 23839 | 0 | 212.12 | 1080.79 | 1169.97 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.65 | 32.59 |
| **Memory (MB)** | 85.90 | 89.62 |
| **Net TX (MB)** | - | 37.02 |
| **Net RX (MB)** | - | 13.68 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 5683 | 258.03 | 0.00 | 253.32 | 28.93 | 79.80 |
| 31 | 6941 | 229.73 | 0.00 | 230.22 | 29.00 | 83.58 |
| 46 | 7570 | 214.77 | 0.00 | 215.27 | 28.89 | 84.99 |

---

## 🧪 Test Run: 2025-10-24 17:32:14

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 80% Read_ID, 10% Read_User, 10% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 10965 | **Total Errors:** 1186 | **Req/Sec:** 178.97

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 9758 | 0 | 498.95 | 1302.44 | 1497.35 |
| **Read (Secondary)** | 0 | 1186 | 0.00 | 0.00 | 0.00 |
| **Write** | 1207 | 0 | 528.76 | 1305.23 | 1501.38 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.00 | 38.31 |
| **Memory (MB)** | 103.04 | 145.28 |
| **Net TX (MB)** | - | 38.77 |
| **Net RX (MB)** | - | 10.54 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 2159 | 644.49 | 0.00 | 681.32 | 34.02 | 123.27 |
| 31 | 2852 | 560.77 | 0.00 | 588.75 | 33.30 | 109.17 |
| 46 | 3077 | 513.97 | 0.00 | 542.38 | 33.09 | 105.17 |
| 61 | 2877 | 498.95 | 0.00 | 528.76 | 33.00 | 103.04 |

---

## 🧪 Test Run: 2025-10-24 17:34:14

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 80% Read_ID, 10% Read_User, 10% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 26805 | **Total Errors:** 3043 | **Req/Sec:** 438.78

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 23867 | 0 | 211.18 | 1082.37 | 1188.04 |
| **Read (Secondary)** | 0 | 3043 | 0.00 | 0.00 | 0.00 |
| **Write** | 2938 | 0 | 218.60 | 1087.50 | 1205.73 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.42 | 33.44 |
| **Memory (MB)** | 85.78 | 88.69 |
| **Net TX (MB)** | - | 44.04 |
| **Net RX (MB)** | - | 21.41 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 5673 | 253.51 | 0.00 | 259.85 | 28.47 | 80.35 |
| 31 | 6993 | 229.65 | 0.00 | 227.68 | 28.73 | 83.73 |
| 46 | 7749 | 211.38 | 0.00 | 216.25 | 28.59 | 85.08 |

---

## 🧪 Test Run: 2025-10-24 17:53:21

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 10% Read_User, 40% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 11497 | **Total Errors:** 1171 | **Req/Sec:** 184.77

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 6371 | 0 | 469.78 | 1271.94 | 1432.49 |
| **Read (Secondary)** | 0 | 1171 | 0.00 | 0.00 | 0.00 |
| **Write** | 5126 | 0 | 501.59 | 1287.93 | 1458.96 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.58 | 39.18 |
| **Memory (MB)** | 166.20 | 176.52 |
| **Net TX (MB)** | - | 22.40 |
| **Net RX (MB)** | - | 8.77 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 2266 | 577.11 | 0.00 | 654.77 | 33.88 | 168.37 |
| 31 | 3031 | 516.57 | 0.00 | 552.48 | 34.41 | 166.77 |
| 46 | 3083 | 489.05 | 0.00 | 519.38 | 33.66 | 166.30 |
| 61 | 3117 | 469.78 | 0.00 | 501.59 | 33.58 | 166.20 |

---

## 🧪 Test Run: 2025-10-24 17:55:15

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | true |
| **ENABLE_SECONDARY_READS** | True |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 50% Read_ID, 10% Read_User, 40% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |

### 📊 Performance Results (Final)
**Total Requests:** 30178 | **Total Errors:** 3418 | **Req/Sec:** 494.41

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 16840 | 0 | 187.25 | 1066.70 | 1137.21 |
| **Read (Secondary)** | 0 | 3418 | 0.00 | 0.00 | 0.00 |
| **Write** | 13338 | 0 | 189.52 | 1067.76 | 1134.41 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.84 | 33.73 |
| **Memory (MB)** | 79.29 | 82.74 |
| **Net TX (MB)** | - | 32.09 |
| **Net RX (MB)** | - | 19.66 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 6176 | 234.20 | 0.00 | 234.90 | 29.98 | 72.73 |
| 31 | 7504 | 210.13 | 0.00 | 215.23 | 28.75 | 76.99 |
| 46 | 9230 | 187.85 | 0.00 | 191.64 | 29.15 | 78.42 |

---

