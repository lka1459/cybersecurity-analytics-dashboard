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
| Rank | Attack | Date | Count |  
|----------|----------|------: | ------: |
| 1 | DoS Hulk | 5/7/17 | 231,073 |
| 2 | PortScan | 7/7/17 | 158,930 |
| 3 | DDoS | 7/7/17 | 128,027 |
| 4 | DoS GoldenEye | 5/7/17 | 10,293 |
| 5 | FTP-Patator | 4/7/17 | 7,938 |
| 6 | SSH-Patator | 4/7/17 | 5,897 |
| 7 | DoS slowloris | 5/7/17 | 5,796 |
| 8 | DoS Slowhttptest | 5/7/17 | 5,499 | 
| 9 | Bot | 7/7/17 | 1,966 |
| 10 | Web Attack (Brute Force) | 6/7/17 | 1,507 | 
| 11 | Web Attack (XSS) | 6/7/17 | 652 |
| 12 | Infiltration | 6/7/17 | 36 |
| 13 | Web Attack (Sql Injection) | 6/7/17 | 21 |
| 14 | Heartbleed | 5/7/17 | 11 |

**Note:** \
BENIGN = 2,273,097 (most overall)\
NaN = 288,602 (second most)

**Observation:** 
DoS Hulk, PortScan and DDoS were the top three types of attack respectively. While Heartbleed was the least frequent attack. 

---

### What are the most common ports used for attacks? (both source and destination)?

**Query:** source_port.sql and dest_port.sql

**Result (Source):**

| Rank | Port | Label |  Count |  
|----------|----------|------: | ------: |
| 1 | 59328 | Portscan | 1003 |
| 2 | 37796 | Portscan | 1002 |
| 3 | 49008 | Portscan | 1000 |
| 4 | 42254 | Portscan | 1000 |
| 5 | 36448 | Portscan | 1000 |
| 6 | 60768 | Portscan | 1000 |
| 7 | 45002 | Portscan | 1000 |
| 8 | 42452 | Portscan | 1000 |
| 9 | 42784 | Portscan | 999 |
| 10 | 55826 | Portscan | 998 |
| 11 | 38444 | Portscan | 997 |
| 12 | 54812 | Portscan | 996 |
| 13 | 46785 | Portscan | 996 |
| 14 | 34110 | Portscan | 996 |

**Result (Destination):**

| Rank | Port | Label |  Count |  
|----------|----------|------: | ------: |
| 1 | 80 | DoS Hulk | 231,073 |
| 2 | 80 | DDoS | 128,024 |
| 3 | 80 | DoS GoldenEye | 10,293 |
| 4 | 21 | FTP-Patator | 7,937 |
| 5 | 22 | SSH-Patator | 5,897 |
| 6 | 80 | DoS slowloris | 5,796 |
| 7 | 80 | DoS Slowhttptest | 5,499 |
| 8 | 80 | Web Attack (Brute Force) | 1507 |
| 9 | 8080 | Bot | 1,261 |
| 10 | 80 | Web Attack (XSS) | 652 |
| 11 | 80 | Portscan | 373 |
| 12 | 21 | Portscan | 244 |
| 13 | 22 | Portscan | 243 |
| 14 | 443 | Portscan | 240 |

**Observation:**
From these observations, it's clear that attackers are using PortScans to identify weakpoints and open ports in the network. Then attackers likely use other attack methods best suited for the exposed ports.

---

### What does the average packet size look like, is there any correlation between benign and malicious packets?

**Query:** avg_packet_size.sql

**Result:**

| Rank | Size | Label |  Count |  
|----------|----------|------: | ------: |
| 1 | NaN | NaN | 288,602 |
| 2 | 0 | BENIGN | 278,666 |
| 3 | 9 | BENIGN | 186,708 |
| 4 | 3 | Portscan | 79,722 |
| 5 | 5 | Portscan | 77,955 |
| 6 | 0 | DoS Hulk | 65,928 |
| 7 | 3 | BENIGN | 55,869 |
| 8 | 4.5 | BENIGN | 33,235 |
| 9 | 7.5 | DDoS | 22,984 |
| 10 | 7.2 | DDoS | 22,283 |
| 11 | 72 | BENIGN | 18,991 |
| 12 | 88.5 | BENIGN | 18,916 |
| 13 | 31 | BENIGN | 16,044 |
| 14 | 8 | BENIGN | 15,730 |

**Observation:** 
There doesn't seem to be anysort of indication of packet size being an indication of malicious or benign activity.

---

### What Source and Destination Ports were used by malicious network packets?

**Query:** source_ip.sql, dest_ip.sql

**Result (Source):**

| Rank | Source IP      | Label                    |   Count |
| ---- | -------------- | ------------------------ | ------: |
| 1    | 172.16.0.1     | DoS Hulk                 | 231,073 |
| 2    | 172.16.0.1     | PortScan                 | 158,930 |
| 3    | 172.16.0.1     | DDoS                     | 128,024 |
| 4    | 172.16.0.1     | DoS GoldenEye            |  10,293 |
| 5    | 172.16.0.1     | FTP-Patator              |   7,938 |
| 6    | 172.16.0.1     | SSH-Patator              |   5,897 |
| 7    | 172.16.0.1     | DoS slowloris            |   5,796 |
| 8    | 172.16.0.1     | DoS Slowhttptest         |   5,499 |
| 9    | 172.16.0.1     | Web Attack Brute Force   |   1,507 |
| 10   | 205.174.165.73 | Bot                      |     705 |
| 11   | 172.16.0.1     | Web Attack XSS           |     652 |
| 12   | 192.168.10.15  | Bot                      |     371 |
| 13   | 192.168.10.8   | Bot                      |     271 |
| 14   | 192.168.10.9   | Bot                      |     226 |
| 15   | 192.168.10.14  | Bot                      |     209 |
| 16   | 192.168.10.5   | Bot                      |     180 |
| 17   | 192.168.10.8   | Infiltration             |      36 |
| 18   | 172.16.0.1     | Web Attack SQL Injection |      21 |
| 19   | 172.16.0.1     | Heartbleed               |      11 |
| 20   | 192.168.10.50  | DDoS                     |       3 |
| 21   | 192.168.10.12  | Bot                      |       2 |
| 22   | 192.168.10.17  | Bot                      |       2 |

**Result (Destination):**

| Rank | Destination IP | Label                    |   Count |
| ---- | -------------- | ------------------------ | ------: |
| 1    | 192.168.10.50  | DoS Hulk                 | 231,073 |
| 2    | 192.168.10.50  | PortScan                 | 158,930 |
| 3    | 192.168.10.50  | DDoS                     | 128,024 |
| 4    | 192.168.10.50  | DoS GoldenEye            |  10,293 |
| 5    | 192.168.10.50  | FTP-Patator              |   7,938 |
| 6    | 192.168.10.50  | SSH-Patator              |   5,897 |
| 7    | 192.168.10.50  | DoS slowloris            |   5,796 |
| 8    | 192.168.10.50  | DoS Slowhttptest         |   5,499 |
| 9    | 192.168.10.50  | Web Attack Brute Force   |   1,507 |
| 10   | 205.174.165.73 | Bot                      |   1,257 |
| 11   | 192.168.10.50  | Web Attack XSS           |     652 |
| 12   | 192.168.10.15  | Bot                      |     209 |
| 13   | 192.168.10.9   | Bot                      |     146 |
| 14   | 192.168.10.14  | Bot                      |     139 |
| 15   | 192.168.10.5   | Bot                      |     108 |
| 16   | 192.168.10.8   | Bot                      |     103 |
| 17   | 205.174.165.73 | Infiltration             |      36 |
| 18   | 192.168.10.50  | Web Attack SQL Injection |      21 |
| 19   | 192.168.10.51  | Heartbleed               |      11 |
| 20   | 172.16.0.1     | DDoS                     |       3 |
| 21   | 52.7.235.158   | Bot                      |       2 |
| 22   | 52.6.13.28     | Bot                      |       2 |

**Observation:**
172.16.0.1 seems to be the main source of attacks while 192.168.10.50 (likely somesort of local network) is the main target/destination of these attacks.

---

### How do attack flows differ from benign flow? 

**Query:** attack_flow.sql

**Result:**

| Rank | Label | Flow Duration | Total Fwd Packets | Total Bwd Packets | Fwd Packets Total Length | Bwd Packets Total Length | Total |
|----------|----------|----------:|----------:|----------:|----------:|----------:|------:|
| 1 | BENIGN | 11,220,820.77 | 10.65 | 12.14 | 635.54 | 18,848.71 | 2,273,097 |
| 2 | DoS Hulk | 57,081,731.89 | 5.28 | 4.21 | 281.33 | 7,770.72 | 231,073 |
| 3 | PortScan | 82,820.23 | 1.02 | 1.00 | 1.09 | 12.24 | 158,930 |
| 4 | DDoS | 16,955,591.77 | 4.47 | 3.26 | 31.91 | 7,373.63 | 128,027 |
| 5 | DoS GoldenEye | 23,127,222.22 | 5.90 | 3.71 | 418.43 | 6,561.32 | 10,293 |
| 6 | FTP-Patator | 4,513,244.60 | 5.50 | 7.81 | 60.03 | 93.91 | 7,938 |
| 7 | SSH-Patator | 6,168,966.83 | 11.12 | 16.53 | 1,008.59 | 1,382.55 | 5,897 |
| 8 | DoS slowloris | 56,554,365.02 | 6.34 | 1.66 | 810.69 | 20.59 | 5,796 |
| 9 | DoS Slowhttptest | 57,719,891.73 | 5.74 | 0.96 | 496.55 | 118.39 | 5,499 |
| 10 | Bot | 350,942.67 | 3.19 | 3.34 | 2,645.45 | 63.80 | 1,966 |
| 11 | Web Attack Brute Force | 6,506,181.63 | 12.37 | 6.06 | 2,111.50 | 3,484.74 | 1,507 |
| 12 | Web Attack XSS | 6,715,357.09 | 7.90 | 3.57 | 1,197.62 | 4,519.02 | 652 |
| 13 | Infiltration | 78,407,720.50 | 830.22 | 829.61 | 376,725.78 | 5,013.67 | 36 |
| 14 | Web Attack SQL Injection | 2,870,398.29 | 3.05 | 2.67 | 316.00 | 1,286.29 | 21 |
| 15 | Heartbleed | 110,679,707.55 | 2,583.73 | 1,897.18 | 12,509.73 | 7,276,360.64 | 11 |

**Observation:** 
Heartbleed and Infiliration attacks seem to have the longest flow durations which indicates that they are the longest attacks. However since they also have so little actual records, this must be taken with a grain of salt. On the other hand, PortScans and Bot attacks which were at the bottom indicating that they were much quicker.

---


### Which attacks had the highest packet transmission rates? 

**Query:** attack_flow.sql

**Result:**
| Rank | Label | Avg Flow Bytes/s | Avg Flow Packets/s | Total |
|------|-------|-----------------:|-------------------:|------:|
| 1 | BENIGN | 1,779,841.56 | 64,778.59 | 2,273,097 |
| 2 | DoS Hulk | 29,401.72 | 182,511.92 | 231,073 |
| 3 | PortScan | 220,359.75 | 62,690.57 | 158,930 |
| 4 | DDoS | 61,117.88 | 172.79 | 128,027 |
| 5 | DoS GoldenEye | 688.24 | 9.14 | 10,293 |
| 6 | FTP-Patator | 799,464.59 | 115,888.89 | 7,938 |
| 7 | SSH-Patator | 439.82 | 15,435.24 | 5,897 |
| 8 | DoS slowloris | 43,921.22 | 4,231.88 | 5,796 |
| 9 | DoS Slowhttptest | 21,642,420.63 | 22,235.78 | 5,499 |
| 10 | Bot | 307,099.15 | 46,841.28 | 1,966 |
| 11 | Web Attack Brute Force | 179.28 | 3,684.90 | 1,507 |
| 12 | Web Attack XSS | 103.35 | 1,565.96 | 652 |
| 13 | Infiltration | 20,188.22 | 2,820.06 | 36 |
| 14 | Web Attack SQL Injection | 318.73 | 12,794.10 | 21 |
| 15 | Heartbleed | 65,902.80 | 40.56 | 11 |

**Observation:** 
DoS Slowhttptest had the average flow btyes indicating extermely high payloads. Meanwhile DoS Hulk had the highest average flow of packets which suggests aggressive packet flooding movement. Additionally, FTP-Patator also had  the second highest average flow btyes and average flow packets indicated heavy packet tranmission.


---
