## 🧪 Test Run: 2025-10-24 19:53:53

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | postgres               |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 24196 | **Total Errors:** 0 | **Req/Sec:** 390.18

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 12112    | 0      | 225.64       | 1098.52  | 1167.60  |
| **Write**          | 12084    | 0      | 232.08       | 1098.68  | 1169.53  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max   |
| :-------------- | :---- | :---- |
| **CPU (%)**     | 29.09 | 34.14 |
| **Memory (MB)** | 94.03 | 97.31 |
| **Net TX (MB)** | -     | 66.33 |
| **Net RX (MB)** | -     | 45.31 |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 5677     | 252.91        | 267.88            | 26.89          | 88.81       |
| 33       | 6480     | 238.87        | 250.22            | 28.24          | 92.63       |
| 48       | 7610     | 222.35        | 228.06            | 29.04          | 93.66       |

---

## 🧪 Test Run: 2025-10-24 19:55:57

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | postgres               |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 19576 | **Total Errors:** 0 | **Req/Sec:** 315.63

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 9838     | 0      | 294.42       | 1130.65  | 1210.44  |
| **Write**          | 9738     | 0      | 271.65       | 1113.58  | 1198.72  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max   |
| :-------------- | :---- | :---- |
| **CPU (%)**     | 29.58 | 33.85 |
| **Memory (MB)** | 82.84 | 85.74 |
| **Net TX (MB)** | -     | 52.98 |
| **Net RX (MB)** | -     | 36.92 |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 4366     | 340.13        | 332.88            | 27.55          | 77.61       |
| 33       | 5137     | 320.67        | 305.09            | 28.84          | 81.00       |
| 48       | 6330     | 291.01        | 271.01            | 29.60          | 82.21       |

---

## 🧪 Test Run: 2025-10-24 20:03:24

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 8678 | **Total Errors:** 0 | **Req/Sec:** 137.21

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 4365     | 0      | 635.92       | 1402.71  | 1531.39  |
| **Write**          | 4313     | 0      | 691.27       | 1418.84  | 1645.36  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 35.02  | 39.54  |
| **Memory (MB)** | 100.15 | 145.91 |
| **Net TX (MB)** | -      | 30.80  |
| **Net RX (MB)** | -      | 23.11  |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 1902     | 717.09        | 825.31            | 32.31          | 111.85      |
| 33       | 2271     | 681.83        | 749.96            | 34.37          | 103.14      |
| 48       | 2458     | 639.16        | 704.00            | 34.62          | 101.01      |
| 63       | 2047     | 635.92        | 691.27            | 35.02          | 100.15      |

---

## 🧪 Test Run: 2025-10-24 20:05:19

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 8675 | **Total Errors:** 0 | **Req/Sec:** 137.17

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 4238     | 0      | 626.45       | 1408.68  | 1588.07  |
| **Write**          | 4437     | 0      | 682.74       | 1415.56  | 1664.95  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 34.49  | 39.95  |
| **Memory (MB)** | 100.84 | 146.98 |
| **Net TX (MB)** | -      | 29.95  |
| **Net RX (MB)** | -      | 22.46  |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 1934     | 695.14        | 813.93            | 31.19          | 112.18      |
| 33       | 2360     | 651.27        | 738.52            | 33.97          | 104.36      |
| 48       | 2445     | 626.24        | 692.80            | 34.56          | 101.91      |
| 63       | 1936     | 626.45        | 682.74            | 34.49          | 100.84      |

---

## 🧪 Test Run: 2025-10-24 20:08:58

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 8635 | **Total Errors:** 0 | **Req/Sec:** 136.51

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 4324     | 0      | 639.45       | 1409.88  | 1597.67  |
| **Write**          | 4311     | 0      | 696.00       | 1443.72  | 1616.66  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max    |
| :-------------- | :---- | :----- |
| **CPU (%)**     | 35.31 | 41.66  |
| **Memory (MB)** | 97.79 | 149.54 |
| **Net TX (MB)** | -     | 31.03  |
| **Net RX (MB)** | -     | 23.29  |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 1865     | 726.60        | 835.88            | 31.48          | 102.18      |
| 33       | 2319     | 674.31        | 753.87            | 34.94          | 98.67       |
| 48       | 2467     | 634.00        | 703.35            | 35.41          | 98.03       |
| 63       | 1984     | 639.45        | 696.00            | 35.31          | 97.79       |

---

## 🧪 Test Run: 2025-10-24 20:12:33

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 13027 | **Total Errors:** 0 | **Req/Sec:** 209.43

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 0        | 0      | 0.00         | 0.00     | 0.00     |
| **Write**          | 13027    | 0      | 435.32       | 1245.39  | 1349.59  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max    |
| :-------------- | :---- | :----- |
| **CPU (%)**     | 32.18 | 35.99  |
| **Memory (MB)** | 99.61 | 147.55 |
| **Net TX (MB)** | -     | 10.97  |
| **Net RX (MB)** | -     | 7.16   |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 2688     | 0.00          | 551.08            | 28.52          | 115.10      |
| 33       | 3424     | 0.00          | 489.28            | 30.65          | 104.24      |
| 48       | 3846     | 0.00          | 448.44            | 31.55          | 101.07      |

---

## 🧪 Test Run: 2025-10-24 20:14:38

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 11960 | **Total Errors:** 0 | **Req/Sec:** 189.03

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 0        | 0      | 0.00         | 0.00     | 0.00     |
| **Write**          | 11960    | 0      | 478.73       | 1270.41  | 1417.56  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 32.41  | 37.86  |
| **Memory (MB)** | 105.03 | 150.08 |
| **Net TX (MB)** | -      | 10.50  |
| **Net RX (MB)** | -      | 6.89   |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 2523     | 0.00          | 582.89            | 30.03          | 120.44      |
| 33       | 3101     | 0.00          | 529.88            | 31.20          | 109.69      |
| 48       | 3665     | 0.00          | 479.52            | 32.52          | 106.75      |
| 63       | 2671     | 0.00          | 478.73            | 32.41          | 105.03      |

---

## 🧪 Test Run: 2025-10-24 20:22:18

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 13144 | **Total Errors:** 0 | **Req/Sec:** 211.37

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 0        | 0      | 0.00         | 0.00     | 0.00     |
| **Write**          | 13144    | 0      | 429.90       | 1238.75  | 1380.34  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 32.47  | 36.79  |
| **Memory (MB)** | 105.86 | 158.72 |
| **Net TX (MB)** | -      | 11.09  |
| **Net RX (MB)** | -      | 7.23   |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 2566     | 0.00          | 570.62            | 28.30          | 116.96      |
| 33       | 3658     | 0.00          | 478.98            | 31.54          | 108.83      |
| 48       | 3897     | 0.00          | 439.13            | 31.94          | 106.76      |

---

## 🧪 Test Run: 2025-10-24 20:24:59

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 13054 | **Total Errors:** 0 | **Req/Sec:** 206.39

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 0        | 0      | 0.00         | 0.00     | 0.00     |
| **Write**          | 13054    | 0      | 434.73       | 1254.19  | 1371.86  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max    |
| :-------------- | :---- | :----- |
| **CPU (%)**     | 31.76 | 36.94  |
| **Memory (MB)** | 98.34 | 146.36 |
| **Net TX (MB)** | -     | 11.30  |
| **Net RX (MB)** | -     | 7.37   |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 2720     | 0.00          | 543.10            | 28.73          | 115.81      |
| 33       | 3463     | 0.00          | 482.63            | 30.77          | 103.87      |
| 48       | 3936     | 0.00          | 439.58            | 31.81          | 100.37      |
| 63       | 2935     | 0.00          | 434.73            | 31.76          | 98.34       |

---

## 🧪 Test Run: 2025-10-24 20:42:15

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 10263 | **Total Errors:** 0 | **Req/Sec:** 164.99

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 5044     | 0      | 544.55       | 2078.54  | 2363.43  |
| **Write**          | 5219     | 0      | 560.05       | 2060.47  | 2360.80  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 30.14  | 40.03  |
| **Memory (MB)** | 100.49 | 144.15 |
| **Net TX (MB)** | -      | 34.20  |
| **Net RX (MB)** | -      | 25.99  |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 19       | 2309     | 693.54        | 694.40            | 28.72          | 105.28      |
| 34       | 2755     | 608.54        | 618.72            | 29.99          | 101.63      |
| 49       | 2839     | 571.26        | 589.94            | 29.84          | 100.86      |

---

## 🧪 Test Run: 2025-10-24 20:45:08

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | mongo                  |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 9242 | **Total Errors:** 0 | **Req/Sec:** 148.15

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 4606     | 0      | 644.32       | 2106.28  | 2392.87  |
| **Write**          | 4636     | 0      | 584.50       | 2089.00  | 2304.00  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg    | Max    |
| :-------------- | :----- | :----- |
| **CPU (%)**     | 30.38  | 38.00  |
| **Memory (MB)** | 102.33 | 145.25 |
| **Net TX (MB)** | -      | 31.31  |
| **Net RX (MB)** | -      | 23.80  |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 19       | 2134     | 761.24        | 738.75            | 27.81          | 111.81      |
| 34       | 2533     | 696.17        | 631.83            | 29.77          | 104.88      |
| 49       | 2590     | 656.99        | 603.70            | 29.85          | 103.13      |

---

## 🧪 Test Run: 2025-10-24 20:48:40

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | postgres               |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 28613 | **Total Errors:** 0 | **Req/Sec:** 460.27

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 14304    | 0      | 190.54       | 1083.38  | 2095.71  |
| **Write**          | 14309    | 0      | 195.74       | 1085.95  | 2084.83  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max   |
| :-------------- | :---- | :---- |
| **CPU (%)**     | 24.78 | 29.40 |
| **Memory (MB)** | 82.79 | 85.58 |
| **Net TX (MB)** | -     | 74.50 |
| **Net RX (MB)** | -     | 51.32 |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 20       | 6334     | 250.48        | 250.61            | 21.98          | 78.87       |
| 35       | 8525     | 206.85        | 207.86            | 24.09          | 81.42       |
| 51       | 8344     | 198.96        | 202.46            | 24.37          | 82.44       |

---

## 🧪 Test Run: 2025-10-24 20:50:42

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | postgres               |
| **USE_INDEX**      | False                  |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 50% Read_ID, 50% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 13796 | **Total Errors:** 0 | **Req/Sec:** 215.63

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 6914     | 0      | 402.31       | 1359.63  | 2173.97  |
| **Write**          | 6882     | 0      | 412.40       | 1354.28  | 2256.81  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max   |
| :-------------- | :---- | :---- |
| **CPU (%)**     | 28.02 | 38.29 |
| **Memory (MB)** | 82.17 | 85.54 |
| **Net TX (MB)** | -     | 38.15 |
| **Net RX (MB)** | -     | 27.13 |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 18       | 3434     | 428.85        | 431.79            | 28.31          | 77.21       |
| 33       | 3889     | 381.66        | 395.68            | 28.01          | 80.54       |
| 49       | 4385     | 372.66        | 383.21            | 29.06          | 81.89       |

---

## 🧪 Test Run: 2025-10-24 22:00:37

### ⚙️ Configuration

| Parameter          | Value                  |
| :----------------- | :--------------------- |
| **DB_TYPE**        | postgres               |
| **USE_INDEX**      | True                   |
| **DATASET_SIZE**   | 50000                  |
| **CONCURRENCY**    | 100                    |
| **DURATION_S**     | 60                     |
| **LOAD_MIX**       | 75% Read_ID, 25% Write |
| **MONITOR_TARGET** | app                    |
| **APP_CPUS**       | 0.5                    |
| **APP_MEM**        | 1g                     |
| **DB_CPUS**        | N/A                    |
| **DB_MEM**         | N/A                    |

### 📊 Performance Results (Final)

**Total Requests:** 22736 | **Total Errors:** 0 | **Req/Sec:** 364.11

| Operation          | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :----------------- | :------- | :----- | :----------- | :------- | :------- |
| **Read (Primary)** | 16969    | 0      | 241.61       | 1102.42  | 2084.97  |
| **Write**          | 5767     | 0      | 253.18       | 1111.15  | 2093.20  |

### 💻 Resource Usage (app - Final)

| Resource        | Avg   | Max   |
| :-------------- | :---- | :---- |
| **CPU (%)**     | 25.97 | 32.72 |
| **Memory (MB)** | 83.93 | 86.70 |
| **Net TX (MB)** | -     | 83.82 |
| **Net RX (MB)** | -     | 57.77 |

### 📈 Periodic Report Log

| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :------- | :------- | :------------ | :---------------- | :------------- | :---------- | :----------- |
| 20       | 5055     | 310.18        | 335.82            | 23.76          | 80.76       |
| 35       | 5388     | 287.74        | 317.19            | 25.64          | 82.70       |
| 51       | 7959     | 250.35        | 263.75            | 25.91          | 83.50       |

---
## 🧪 Test Run: 2025-10-24 22:06:47

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 75% Read_ID, 25% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 19791 | **Total Errors:** 0 | **Req/Sec:** 318.34

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 14821 | 0 | 282.64 | 1139.29 | 2116.27 |
| **Write** | 4970 | 0 | 272.88 | 1123.56 | 2108.44 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.37 | 31.04 |
| **Memory (MB)** | 83.96 | 86.58 |
| **Net TX (MB)** | - | 71.10 |
| **Net RX (MB)** | - | 49.56 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 4525 | 354.37 | 343.05 | 23.70 | 79.97 |
| 35 | 5557 | 306.06 | 304.02 | 25.70 | 82.62 |
| 50 | 5624 | 291.28 | 285.76 | 25.74 | 83.47 |

---

## 🧪 Test Run: 2025-10-24 22:09:06

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 75% Read_ID, 25% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 9436 | **Total Errors:** 0 | **Req/Sec:** 151.72

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 7068 | 0 | 592.51 | 2092.70 | 2333.08 |
| **Write** | 2368 | 0 | 623.88 | 2093.66 | 2322.06 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 31.34 | 39.54 |
| **Memory (MB)** | 99.11 | 144.18 |
| **Net TX (MB)** | - | 43.47 |
| **Net RX (MB)** | - | 33.53 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2053 | 696.52 | 765.50 | 27.92 | 107.97 |
| 33 | 2619 | 621.29 | 674.87 | 30.76 | 101.42 |
| 48 | 2533 | 615.39 | 654.69 | 31.10 | 99.74 |

---

## 🧪 Test Run: 2025-10-24 22:11:08

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 75% Read_ID, 25% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 6742 | **Total Errors:** 0 | **Req/Sec:** 107.81

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5076 | 0 | 862.12 | 2191.80 | 2599.69 |
| **Write** | 1666 | 0 | 804.87 | 2157.04 | 2606.35 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 33.68 | 43.32 |
| **Memory (MB)** | 102.01 | 145.23 |
| **Net TX (MB)** | - | 32.89 |
| **Net RX (MB)** | - | 25.44 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1592 | 917.13 | 1025.61 | 32.70 | 112.63 |
| 33 | 1740 | 898.13 | 919.10 | 34.18 | 104.85 |
| 49 | 1977 | 876.67 | 845.93 | 33.57 | 102.69 |

---

## 🧪 Test Run: 2025-10-24 22:14:00

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 25% Read_ID, 75% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 11918 | **Total Errors:** 0 | **Req/Sec:** 191.35

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 3032 | 0 | 485.02 | 2043.50 | 2268.26 |
| **Write** | 8886 | 0 | 474.47 | 1606.93 | 2231.87 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.86 | 38.96 |
| **Memory (MB)** | 98.85 | 143.65 |
| **Net TX (MB)** | - | 25.16 |
| **Net RX (MB)** | - | 18.52 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 2536 | 638.42 | 629.75 | 27.14 | 108.97 |
| 34 | 3396 | 531.88 | 520.59 | 28.66 | 102.08 |
| 49 | 3322 | 504.72 | 491.15 | 28.56 | 99.76 |

---

## 🧪 Test Run: 2025-10-24 22:16:10

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 25% Read_ID, 75% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 10273 | **Total Errors:** 0 | **Req/Sec:** 164.75

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 2566 | 0 | 604.71 | 2062.10 | 2284.16 |
| **Write** | 7707 | 0 | 532.92 | 2042.49 | 2269.98 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 28.48 | 35.55 |
| **Memory (MB)** | 102.58 | 147.81 |
| **Net TX (MB)** | - | 22.23 |
| **Net RX (MB)** | - | 16.37 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 2148 | 681.30 | 680.46 | 25.67 | 115.79 |
| 33 | 2758 | 645.08 | 591.08 | 27.65 | 106.54 |
| 48 | 2797 | 633.06 | 566.19 | 28.05 | 103.63 |

---

## 🧪 Test Run: 2025-10-24 22:18:20

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 25% Read_ID, 75% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 29932 | **Total Errors:** 0 | **Req/Sec:** 480.58

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 7512 | 0 | 179.88 | 1068.35 | 2075.30 |
| **Write** | 22420 | 0 | 186.85 | 1072.82 | 2077.55 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 24.35 | 29.95 |
| **Memory (MB)** | 82.71 | 85.98 |
| **Net TX (MB)** | - | 50.76 |
| **Net RX (MB)** | - | 35.61 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 6731 | 214.24 | 243.28 | 21.74 | 78.15 |
| 35 | 9108 | 187.94 | 196.13 | 23.98 | 80.95 |
| 50 | 8556 | 178.59 | 188.07 | 24.09 | 82.15 |

---

## 🧪 Test Run: 2025-10-24 22:21:02

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 25% Read_ID, 75% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 25718 | **Total Errors:** 0 | **Req/Sec:** 412.89

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 6523 | 0 | 221.27 | 1141.09 | 2116.45 |
| **Write** | 19195 | 0 | 214.42 | 1129.98 | 2120.95 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 25.84 | 31.86 |
| **Memory (MB)** | 82.93 | 85.21 |
| **Net TX (MB)** | - | 43.66 |
| **Net RX (MB)** | - | 31.09 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 6200 | 263.75 | 254.81 | 22.85 | 78.67 |
| 35 | 7503 | 229.61 | 223.05 | 25.48 | 81.53 |
| 51 | 7682 | 220.90 | 217.58 | 25.62 | 82.58 |

---

## 🧪 Test Run: 2025-10-24 22:23:13

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 100% Read_ID, 0% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 24886 | **Total Errors:** 0 | **Req/Sec:** 399.60

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 24886 | 0 | 222.74 | 1100.44 | 2086.61 |
| **Write** | 0 | 0 | 0.00 | 0.00 | 0.00 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 25.35 | 31.74 |
| **Memory (MB)** | 90.45 | 93.20 |
| **Net TX (MB)** | - | 117.24 |
| **Net RX (MB)** | - | 80.26 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 5618 | 281.32 | 0.00 | 22.69 | 86.94 |
| 35 | 7524 | 233.12 | 0.00 | 24.98 | 89.40 |
| 51 | 7698 | 223.04 | 0.00 | 25.29 | 90.25 |

---

## 🧪 Test Run: 2025-10-24 22:25:12

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 100% Read_ID, 0% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 17103 | **Total Errors:** 0 | **Req/Sec:** 275.08

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 17103 | 0 | 326.93 | 1210.36 | 2187.93 |
| **Write** | 0 | 0 | 0.00 | 0.00 | 0.00 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.85 | 35.64 |
| **Memory (MB)** | 82.57 | 85.57 |
| **Net TX (MB)** | - | 80.81 |
| **Net RX (MB)** | - | 56.16 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 3984 | 401.20 | 0.00 | 23.98 | 79.11 |
| 34 | 5257 | 334.56 | 0.00 | 25.90 | 81.22 |
| 49 | 5562 | 308.23 | 0.00 | 25.96 | 82.17 |

---

## 🧪 Test Run: 2025-10-24 22:27:23

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 100% Read_ID, 0% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 8670 | **Total Errors:** 0 | **Req/Sec:** 139.15

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 8670 | 0 | 653.72 | 2139.50 | 2437.39 |
| **Write** | 0 | 0 | 0.00 | 0.00 | 0.00 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 31.22 | 38.63 |
| **Memory (MB)** | 99.36 | 144.82 |
| **Net TX (MB)** | - | 51.01 |
| **Net RX (MB)** | - | 39.64 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1899 | 771.28 | 0.00 | 28.65 | 107.89 |
| 33 | 2454 | 678.60 | 0.00 | 31.36 | 102.06 |
| 48 | 2214 | 685.36 | 0.00 | 30.93 | 100.20 |

---

## 🧪 Test Run: 2025-10-24 22:30:11

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 50000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 100% Read_ID, 0% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 5658 | **Total Errors:** 0 | **Req/Sec:** 90.46

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5658 | 0 | 1004.62 | 2419.53 | 2778.07 |
| **Write** | 0 | 0 | 0.00 | 0.00 | 0.00 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 36.87 | 48.39 |
| **Memory (MB)** | 98.29 | 143.47 |
| **Net TX (MB)** | - | 34.56 |
| **Net RX (MB)** | - | 26.99 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 1288 | 1130.02 | 0.00 | 34.62 | 106.52 |
| 33 | 1385 | 1095.95 | 0.00 | 37.59 | 100.03 |
| 48 | 1589 | 1060.91 | 0.00 | 37.08 | 98.52 |

---

## 🧪 Test Run: 2025-10-24 23:53:53

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
**Total Requests:** 16803 | **Total Errors:** 0 | **Req/Sec:** 269.89

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 16803 | 0 | 336.65 | 1195.35 | 2111.60 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.90 | 33.79 |
| **Memory (MB)** | 99.19 | 145.55 |
| **Net TX (MB)** | - | 13.69 |
| **Net RX (MB)** | - | 8.73 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 3035 | 0.00 | 488.33 | 24.55 | 111.24 |
| 33 | 4868 | 0.00 | 375.46 | 26.52 | 102.91 |
| 48 | 4799 | 0.00 | 355.05 | 26.80 | 100.24 |

---

## 🧪 Test Run: 2025-10-24 23:56:36

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
**Total Requests:** 16290 | **Total Errors:** 0 | **Req/Sec:** 261.19

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 16290 | 0 | 348.03 | 1185.80 | 2159.36 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.48 | 33.53 |
| **Memory (MB)** | 97.35 | 146.89 |
| **Net TX (MB)** | - | 13.45 |
| **Net RX (MB)** | - | 8.59 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 3381 | 0.00 | 473.90 | 24.35 | 108.10 |
| 34 | 4814 | 0.00 | 378.65 | 26.08 | 100.78 |
| 49 | 4965 | 0.00 | 347.69 | 26.22 | 98.37 |

---

## 🧪 Test Run: 2025-10-24 23:59:03

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
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
**Total Requests:** 35847 | **Total Errors:** 0 | **Req/Sec:** 575.03

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 35847 | 0 | 154.62 | 1045.30 | 2053.81 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 23.80 | 28.82 |
| **Memory (MB)** | 83.20 | 86.15 |
| **Net TX (MB)** | - | 23.01 |
| **Net RX (MB)** | - | 17.66 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 7815 | 0.00 | 203.95 | 21.63 | 78.85 |
| 35 | 10860 | 0.00 | 165.02 | 23.50 | 81.82 |
| 51 | 10712 | 0.00 | 158.42 | 23.73 | 82.91 |

---

## 🧪 Test Run: 2025-10-25 00:01:05

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
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
**Total Requests:** 31515 | **Total Errors:** 0 | **Req/Sec:** 504.50

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 31515 | 0 | 175.44 | 1063.96 | 2080.70 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 24.41 | 31.11 |
| **Memory (MB)** | 83.02 | 85.88 |
| **Net TX (MB)** | - | 20.42 |
| **Net RX (MB)** | - | 15.65 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 8481 | 0.00 | 184.53 | 21.84 | 77.87 |
| 35 | 10363 | 0.00 | 160.82 | 23.93 | 81.41 |
| 51 | 8867 | 0.00 | 166.73 | 24.22 | 82.69 |

---

## 🧪 Test Run: 2025-10-25 12:55:10

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 39535 | **Total Errors:** 0 | **Req/Sec:** 633.65

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 39535 | 0 | 138.75 | 1052.07 | 2040.79 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 23.36 | 29.34 |
| **Memory (MB)** | 83.95 | 86.94 |
| **Net TX (MB)** | - | 24.81 |
| **Net RX (MB)** | - | 18.99 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 8937 | 0.00 | 175.45 | 21.16 | 79.02 |
| 35 | 11827 | 0.00 | 146.02 | 22.92 | 82.31 |
| 51 | 11881 | 0.00 | 140.82 | 23.20 | 83.53 |

---

## 🧪 Test Run: 2025-10-25 12:57:23

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 35526 | **Total Errors:** 0 | **Req/Sec:** 569.45

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 35526 | 0 | 155.49 | 1047.97 | 2044.70 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 22.66 | 29.75 |
| **Memory (MB)** | 79.63 | 82.94 |
| **Net TX (MB)** | - | 22.38 |
| **Net RX (MB)** | - | 17.13 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 7406 | 0.00 | 213.29 | 21.05 | 75.87 |
| 35 | 10698 | 0.00 | 168.49 | 22.34 | 78.70 |
| 51 | 11001 | 0.00 | 159.25 | 22.36 | 79.32 |

---

## 🧪 Test Run: 2025-10-25 13:00:35

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | True |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 17588 | **Total Errors:** 0 | **Req/Sec:** 283.22

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 17588 | 0 | 320.69 | 1217.77 | 2121.87 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.50 | 33.68 |
| **Memory (MB)** | 93.08 | 103.02 |
| **Net TX (MB)** | - | 13.27 |
| **Net RX (MB)** | - | 8.31 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 3473 | 0.00 | 458.30 | 24.23 | 93.59 |
| 34 | 5257 | 0.00 | 354.29 | 25.89 | 93.13 |
| 49 | 5192 | 0.00 | 328.34 | 26.09 | 93.13 |

---

## 🧪 Test Run: 2025-10-25 13:02:42

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
| **DATASET_SIZE** | 20000 |
| **CONCURRENCY** | 100 |
| **DURATION_S** | 60 |
| **LOAD_MIX** | 0% Read_ID, 100% Write |
| **MONITOR_TARGET** | app |
| **APP_CPUS** | 0.5 |
| **APP_MEM** | 1g |
| **DB_CPUS** | N/A |
| **DB_MEM** | N/A |

### 📊 Performance Results (Final)
**Total Requests:** 17652 | **Total Errors:** 0 | **Req/Sec:** 284.24

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 0 | 0 | 0.00 | 0.00 | 0.00 |
| **Write** | 17652 | 0 | 319.66 | 1152.63 | 2168.90 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 26.57 | 33.05 |
| **Memory (MB)** | 93.23 | 103.85 |
| **Net TX (MB)** | - | 13.32 |
| **Net RX (MB)** | - | 8.34 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 3372 | 0.00 | 475.38 | 23.94 | 93.12 |
| 34 | 5198 | 0.00 | 361.76 | 26.05 | 92.90 |
| 50 | 5476 | 0.00 | 334.81 | 26.22 | 93.12 |

---

## 🧪 Test Run: 2025-10-25 13:06:16

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
**Total Requests:** 11266 | **Total Errors:** 0 | **Req/Sec:** 181.09

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5608 | 0 | 499.52 | 2039.68 | 2272.41 |
| **Write** | 5658 | 0 | 505.03 | 2049.64 | 2277.72 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 29.54 | 36.38 |
| **Memory (MB)** | 93.22 | 98.37 |
| **Net TX (MB)** | - | 35.50 |
| **Net RX (MB)** | - | 26.91 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 2368 | 667.05 | 684.40 | 26.89 | 90.35 |
| 34 | 3265 | 554.35 | 547.79 | 29.26 | 91.94 |
| 49 | 3055 | 525.76 | 526.24 | 29.16 | 92.65 |

---

## 🧪 Test Run: 2025-10-25 13:10:30

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | mongo |
| **USE_INDEX** | False |
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
**Total Requests:** 10413 | **Total Errors:** 0 | **Req/Sec:** 166.70

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 5233 | 0 | 556.90 | 1521.04 | 2347.71 |
| **Write** | 5180 | 0 | 536.94 | 1605.52 | 2288.15 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 31.06 | 37.49 |
| **Memory (MB)** | 94.15 | 100.71 |
| **Net TX (MB)** | - | 34.93 |
| **Net RX (MB)** | - | 26.52 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 2154 | 730.88 | 756.78 | 27.36 | 91.72 |
| 34 | 3242 | 582.44 | 560.03 | 30.45 | 93.15 |
| 49 | 2775 | 573.02 | 552.87 | 30.66 | 93.80 |

---

## 🧪 Test Run: 2025-10-25 13:12:47

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
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
**Total Requests:** 29792 | **Total Errors:** 0 | **Req/Sec:** 477.73

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 14892 | 0 | 187.55 | 1081.79 | 2071.03 |
| **Write** | 14900 | 0 | 185.32 | 1075.61 | 2053.59 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 24.69 | 32.98 |
| **Memory (MB)** | 81.31 | 83.59 |
| **Net TX (MB)** | - | 78.47 |
| **Net RX (MB)** | - | 53.50 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | 6894 | 229.52 | 230.32 | 22.36 | 77.23 |
| 35 | 8681 | 195.07 | 200.50 | 24.25 | 79.93 |
| 51 | 9025 | 190.51 | 188.80 | 24.50 | 80.98 |

---

## 🧪 Test Run: 2025-10-25 13:15:24

### ⚙️ Configuration
| Parameter | Value |
| :--- | :--- |
| **DB_TYPE** | postgres |
| **USE_INDEX** | False |
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
**Total Requests:** 27466 | **Total Errors:** 0 | **Req/Sec:** 432.97

| Operation | Requests | Errors | Avg Lat (ms) | p95 (ms) | p99 (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Read (Primary)** | 13738 | 0 | 204.88 | 1082.56 | 2074.03 |
| **Write** | 13728 | 0 | 206.70 | 1083.50 | 2082.52 |

### 💻 Resource Usage (app - Final)
| Resource | Avg | Max |
| :--- | :--- | :--- |
| **CPU (%)** | 25.70 | 30.63 |
| **Memory (MB)** | 80.72 | 83.73 |
| **Net TX (MB)** | - | 73.13 |
| **Net RX (MB)** | - | 50.09 |

### 📈 Periodic Report Log
| Time (s) | New Reqs | Read Avg (ms) | Sec.Read Avg (ms) | Write Avg (ms) | CPU Avg (%) | Mem Avg (MB) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 18 | 7271 | 200.03 | 202.37 | 25.07 | 76.06 |
| 34 | 7038 | 206.16 | 208.89 | 25.40 | 79.20 |
| 50 | 7671 | 205.74 | 209.25 | 25.56 | 80.28 |

---

