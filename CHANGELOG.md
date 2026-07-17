## v0.1.0 — Initial project setup and data ingestion
- Created PostgreSQL database
- Imported CIC-IDS2017 datasets
- Established project structure

## v0.2.0 — Added first analysis workflow and improved repo structure
- Created the 01_analysis notebook
- Performed initial analysis on the Friday_Working_Hours_DDOS table
- Removed the notebook folder from gitignore
- Polished up experiments notebook and requirements.txt

## v0.2.1 — Switched to original CIC-IDS2017 flows and rebuilt database
- Changed cleaned Kaggle dataset to original CIC-IDS2017 (same but more uncleaned features)
- Rebuilt the database

## v0.2.2 — Improved database importing workflow
- Refined table naming logic to use underscores instead of dashes
- Updated analysis notebook to fit changes

## v0.2.3 — Update Summary
- Added docs/ folder with dataset_exploration.md
- Introduced analytics.py for early analysis utilities
- Created a new database view to simplify queries
- Added SQL files and a helper function to load them and print DataFrames for quick analysis

## v0.2.4 — Further analysis
- Created several SQL files and analysed ports, IP addresses and packet size
- Adjusted exisiting SQL queries to improve clarity
- Updated dataset_exploration.md with new results