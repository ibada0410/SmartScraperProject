<div align="center">

# 🕷️ Smart Web Scraping & Data Analysis System

**An automated, end-to-end data engineering pipeline — from raw HTML to interactive dashboards.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-4B8BBE?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)](https://matplotlib.org/)

</div>

---

## 📖 Overview

**Smart Web Scraping & Data Analysis System** is a fully automated web scraping pipeline that collects structured data from e-commerce websites, processes and cleans it, stores it in multiple formats, and presents it through beautiful charts and an interactive dashboard.

Built as a real-world demonstration of **data engineering fundamentals** — from raw HTTP requests to a production-ready Streamlit interface.

> 🎯 **Target Website:** [Books to Scrape](https://books.toscrape.com/) — a sandbox e-commerce site for practicing web scraping.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌐 **Multi-page Scraping** | Automatically traverses and scrapes all paginated results |
| 📦 **Data Extraction** | Captures title, price, rating, availability, and image URL |
| 🧹 **Data Cleaning** | Preprocesses and normalizes raw scraped content |
| 💾 **Multi-format Storage** | Saves data as CSV, Excel (`.xlsx`), and SQLite database |
| 📋 **Automated Logging** | Timestamped logs for every scraping session |
| 🔁 **Error Handling & Retry** | Resilient scraping with built-in retry mechanism |
| 📊 **Data Visualization** | Auto-generated bar charts for data insights |
| 🖥️ **Interactive Dashboard** | Streamlit-powered UI for filtering and exploring data |
| 🗂️ **Clean Project Structure** | Organized output folders for logs, data, and charts |

---

## 🧰 Tech Stack

```
Python 3.8+          → Core language
BeautifulSoup4       → HTML parsing & scraping
Requests             → HTTP requests with retry support
Pandas               → Data manipulation & export
SQLite3              → Lightweight relational database
Matplotlib           → Chart generation
openpyxl             → Excel file support
Streamlit            → Interactive web dashboard
```

---

## 📁 Project Structure

```
SmartScraperProject/
│
├── 📂 logs/                  # Scraper session logs
│   └── scraper.log
│
├── 📂 data/                  # All output datasets
│   ├── books.csv             # CSV format
│   ├── books.xlsx            # Excel format
│   └── books.db              # SQLite database
│
├── 📂 charts/                # Generated visualizations
│   └── chart.png
│
├── scraper.py                # 🔧 Main web scraping script
├── chart.py                  # 📊 Chart generation script
├── dashboard.py              # 🖥️ Streamlit dashboard app
└── README.md                 # 📄 Project documentation
```

---

## 📥 Prerequisites

Make sure the following are installed on your system before getting started:

- ✅ **Python 3.8** or higher
- ✅ **pip** package manager
- ✅ Active **internet connection**

---

## 🔧 Installation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-scraper.git
cd SmartScraperProject
```

### Step 2 — Install Dependencies

```bash
pip install requests beautifulsoup4 pandas matplotlib openpyxl streamlit
```

---

## 🚀 Running the Project

### Step 1 — Run the Web Scraper

```bash
python scraper.py
```

**What this does:**
- 🌐 Scrapes all book data from the target website
- 💾 Saves output files to the `/data` folder
- 📋 Writes session logs to the `/logs` folder

---

### Step 2 — Generate Visualizations

```bash
python chart.py
```

**Output:**
```
charts/chart.png   ← Rating distribution bar chart
```

---

### Step 3 — Launch the Dashboard

```bash
python -m streamlit run dashboard.py
```

Then open your browser and visit:

```
http://localhost:8501
```

---

## 📊 Output Files

After a full run, the following files are generated:

```
📄 data/books.csv          → Raw dataset (spreadsheet-compatible)
📊 data/books.xlsx         → Formatted Excel report
🗃️  data/books.db           → SQLite database for querying
📋 logs/scraper.log        → Session log with timestamps
🖼️  charts/chart.png        → Rating distribution visualization
```

---

## 🧪 Key Functionalities

### 🔹 Web Scraping (`scraper.py`)
- Sends paginated HTTP requests to [Books to Scrape](https://books.toscrape.com/)
- Parses HTML with BeautifulSoup to extract:
  - 📚 Book title
  - 💰 Price
  - ⭐ Star rating
  - 📦 Availability
  - 🖼️ Image URL
- Handles retries and network errors gracefully

### 🔹 Data Storage (`scraper.py`)
- **CSV** → For quick analysis and spreadsheet import
- **Excel** → For formatted reporting and sharing
- **SQLite** → For structured querying with SQL

### 🔹 Visualization (`chart.py`)
- Generates a **bar chart** showing the distribution of book ratings
- Saves as `charts/chart.png`

### 🔹 Dashboard (`dashboard.py`)
- Interactive **Streamlit** interface featuring:
  - Full dataset table view
  - Filter by star rating
  - Real-time data exploration

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---|---|
| `streamlit: command not found` | Run `pip install streamlit` |
| `No space left on device` | Free up disk space and retry |
| `books.csv` not generated | Check `logs/scraper.log` for errors |
| Dashboard not opening in browser | Use `python -m streamlit run dashboard.py` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` or install missing package manually |

---

## 🧠 Learning Outcomes

This project is a practical showcase of the following skills:

- 🕷️ **Web Scraping** — Real-world multi-page data extraction
- 🔧 **Data Engineering** — Building an automated pipeline from scratch
- 🗂️ **File Handling** — Working with CSV, Excel, and binary DB files
- 🗃️ **Database Integration** — Storing and querying data with SQLite
- 📊 **Data Visualization** — Creating insightful charts with Matplotlib
- 🖥️ **Dashboard Development** — Building interactive UIs with Streamlit
- 🔁 **Automation Workflow** — Chaining scripts into a reproducible pipeline

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ using Python

⭐ **Star this repo if you found it helpful!**

</div>
