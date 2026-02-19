# 🎉 Pixie – Event Scraper & Analytics Platform

A production-style event scraping and analytics system that collects live event data from **District by Zomato**, syncs it to **Google Sheets**, and displays real-time analytics on a **Streamlit dashboard**.

Built for the Pixie Full Stack Developer Intern Assignment.

---

## 🚀 Architecture Overview

This project follows a clean production workflow:

```
Local Scraper (Selenium)
        ↓
Google Sheet (Central Database)
        ↓
Streamlit Dashboard (Reads Google Sheet)
```

### Why this architecture?

- Selenium works reliably locally
- Google Sheets acts as a lightweight database
- Dashboard remains cloud-compatible
- Clean separation of scraping and analytics

---

## 🌐 Data Source

Events are collected from:

**District by Zomato**  
https://www.district.in

The scraper visits multiple category pages for a selected city.

Example URL format:

```
https://www.district.in/events/{category}-in-{city}-book-tickets
```

### Categories Covered

- music  
- nightlife  
- comedy-shows  
- sports-events  
- performances  
- food-drinks  
- fests-fairs  
- social-mixers  
- openmics  

---

## ✅ Features

✔ Scrapes only EVENTS (no movies)  
✔ Works for multiple cities (mumbai, jaipur, delhi, etc.)  
✔ Covers multiple categories per city  
✔ Deduplicates events using event URL  
✔ Stores structured data  
✔ Syncs entire dataset to Google Sheets  
✔ Dashboard reads live data from Google Sheets  
✔ City-based filtering in dashboard  
✔ Clean full-stack separation  

---

## 📊 Fields Collected

Each event includes:

- `event_name`
- `date`
- `venue`
- `city`
- `category`
- `url`
- `status`
- `last_seen`

---

## 🛠 Tech Stack

### Backend (Scraper)
- Python 3
- Selenium (JS rendering support)
- openpyxl (Excel handling)
- gspread (Google Sheets API)
- Google Service Account Authentication

### Dashboard
- Streamlit
- Pandas
- Google Sheets (data source)

---

## 📂 Project Structure

```
pixil/
│
├── main.py              → Scheduler + scraper runner
├── scraper.py           → Selenium scraping logic
├── storage.py           → Excel storage & deduplication
├── sheets.py            → Google Sheets sync logic
├── dashboard.py         → Streamlit analytics dashboard
├── service_account.json → Google API credentials (local only)
├── events.xlsx          → Local structured dataset
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Run Scraper Locally

```
py main.py --city mumbai
```

This will:
- Scrape all categories
- Deduplicate events
- Update local Excel file
- Sync data to Google Sheet

---

### 2️⃣ Run Dashboard

```
streamlit run dashboard.py
```

The dashboard:
- Reads live data from Google Sheets
- Allows city filtering
- Shows analytics:
  - Total events
  - Active vs Expired
  - Category distribution
  - Venue distribution
  - Full data table

---

## 🔁 Deduplication Strategy

Each event is uniquely identified by:

```
event URL
```

Before inserting new data:
- Existing URLs are checked
- Duplicate entries are skipped

---

## ⏳ Expiry Handling

If an event is not detected in a new scrape:
- It is marked as **Expired**
- Status is updated accordingly

---

## 🔄 Google Sheets Sync Strategy

- Entire Excel dataset is read
- Google Sheet is cleared
- Fresh rows are inserted
- Ensures dashboard always reflects latest data

---

## 🧠 Scheduling

`main.py` supports automated execution at intervals.

Can be extended with:
- Python loop scheduling
- Windows Task Scheduler
- Cron job (Linux/Mac)

---

## 🔐 Security

- Google Service Account used for authentication
- Credentials are NOT committed to GitHub
- Google Sheet shared only with service account

---

## 🎯 Final Output

✔ Live Google Sheet auto-updated  
✔ Public Streamlit Dashboard  
✔ Real scraped event data  
✔ Clean full-stack architecture  

---

## 👨‍💻 Author

Chetan Rajawat  
Full Stack Developer Intern Candidate

---
