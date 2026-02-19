# Pixie – Event Discovery & Tracking Tool

A Python automation tool that discovers upcoming events for a selected city from **District by Zomato**, stores them in Excel, and automatically updates the data at regular intervals.

Built for the Pixie Full Stack Developer Intern assignment.

---

## Data Source

Events are collected from  
:contentReference[oaicite:0]{index=0}  
Owned by :contentReference[oaicite:1]{index=1}

District organizes events by **city + category pages**, so this tool:
- visits multiple category URLs
- extracts events
- merges results
- removes duplicates

---

## Features

✔ Scrapes events automatically  
✔ Works for any city (mumbai, jaipur, delhi, etc.)  
✔ Covers multiple categories (music, sports, comedy, nightlife, etc.)  
✔ Saves data to Excel (.xlsx)  
✔ Deduplicates events  
✔ Marks expired events  
✔ Runs every 2 minutes automatically  
✔ Fully automated  

---

## Tech Stack

- Python 3
- Selenium (dynamic JS rendering)
- openpyxl (Excel writing)
- argparse
- scheduling loop

---

## Project Structure

pixil/
│
├── main.py → scheduler + runner
├── scraper.py → scraping logic
├── storage.py → Excel storage & dedupe logic
├── events.xlsx → generated output file
└── README.md

## How to Run

Basic command
py main.py --city mumbai

