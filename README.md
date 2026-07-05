# Cybersecurity Analytics Dashboard

A Python and PostgreSQL project for analysing network traffic and cybersecurity datasets through SQL queries, data visualisation, and interactive dashboards.

The project focuses on building a complete data analytics workflow, including importing raw CSV files into PostgreSQL, querying the data with SQL, and presenting insights using Python.

## Project Goals

- Build and manage a PostgreSQL database from raw CSV datasets
- Practise writing SQL queries for cybersecurity data analysis
- Create interactive dashboards using Streamlit
- Explore network traffic patterns and security events

## Technologies

- Python
- PostgreSQL
- SQLAlchemy
- pandas
- Streamlit *(planned)*
- Plotly *(planned)*

## Project Workflow

```text
Raw CSV Files
        ↓
PostgreSQL Database
        ↓
SQL Queries
        ↓
Python Analysis
        ↓
Interactive Dashboard
```

## Dataset

This project uses the **CIC-IDS2017** intrusion detection dataset.

Source:
https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

The dataset contains network traffic captured under both normal and malicious conditions, including attacks such as DDoS, Port Scanning, Brute Force, Botnet, and Web Attacks.