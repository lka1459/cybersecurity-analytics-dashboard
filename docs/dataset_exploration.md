# Dataset Exploration

## Overview

**Dataset:** CIC-IDS2017

**Tables:**
- Monday
- Tuesday
- Wednesday
- Thursday Morning (Web Attacks)
- Thursday Afternoon (Infiltration)
- Friday Morning
- Friday Afternoon (DDoS)
- Friday Afternoon (Port scan)


---

## Initial Questions

### What protocols exist?

**Query:** existing_protocols.sql

**Result:**

| Protocol | Count |
|----------|------:|
| TCP | 1,829,554 |
| UDP | 999,493 |
| NaN | 290,298 |

**Observation:**
TCP and UDP are the only protocols present within this dataset. Everything else (including protocol '0') are simply missing values.

---

### Which attack occurs most frequently?

**Query:** total_attacks.sql

**Result:**
| Rank | Attack | Count |  
|----------|----------|------: |
| 1 | DoS Hulk | 231,073 |
| 2 | PortScan | 158,930 |
| 3 | DDoS | 128,027 |
| 4 | DoS GoldenEye | 10,293 |
| 5 | FTP-Patator | 7,938 |
| 6 | SSH-Patator | 5,897 |
| 7 | DoS slowloris | 5,796 |
| 8 | DoS Slowhttptest | 5,499 |
| 9 | Bot | 1,966 |
| 10 | Web Attack (Brute Force) | 1,507 |
| 11 | Web Attack (XSS) | 652 |
| 12 | Infiltration | 36 |
| 13 | Web Attack (Sql Injection) | 21 |
| 14 | Heartbleed | 11 |

**Note:** \
BENIGN = 2,273,097 (most overall)\
NaN = 288,602 (second most)



**Observation:** 
DoS Hulk, PortScan and DDoS were the top three types of attack respectively. While Heartbleed was the least frequent attack. 