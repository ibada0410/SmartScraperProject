🕷️ Smart Web Scraping \& Data Analysis System



A Python-based automated web scraping pipeline that extracts book data from websites, processes it, and stores it in multiple formats (CSV, Excel, SQLite) with logging, visualization, and dashboard support.



📖 Introduction



This project is an automated web scraping system that collects data from an e-commerce website (Books to Scrape), cleans it, and stores it in structured formats including CSV, Excel, and SQLite database.



It also generates logs, visual charts, and an interactive Streamlit dashboard for data exploration.



The goal is to demonstrate real-world data engineering skills including web scraping, data processing, storage management, and visualization.



⚙️ Features



✅ Multi-page web scraping

✅ Data extraction (title, price, rating, availability, image URL)

✅ Data cleaning \& preprocessing

✅ CSV, Excel, and SQLite storage

✅ Automated logging system

✅ Error handling \& retry mechanism

✅ Data visualization (charts)

✅ Interactive Streamlit dashboard

✅ Clean folder structure (logs/data/charts)



🧰 Tech Stack

Python 3.8+

BeautifulSoup4

Requests

Pandas

SQLite3

Matplotlib

Streamlit

📁 Project Structure

SmartScraperProject/

├── logs/                         # Log files

│   └── scraper.log

│

├── data/                         # Scraped datasets

│   ├── books.csv

│   ├── books.xlsx

│   └── books.db

│

├── charts/                       # Data visualizations

│   └── chart.png

│

├── scraper.py                    # Main web scraper

├── chart.py                      # Data visualization script

├── dashboard.py                  # Streamlit dashboard

└── README.md                     # Project documentation

📥 Prerequisites



Before running this project, ensure you have:



Python 3.8 or higher

pip package manager

Internet connection

🔧 Installation

Step 1: Clone or Download Project

git clone https://github.com/YOUR\_USERNAME/smart-scraper.git

cd SmartScraperProject

Step 2: Install Dependencies

pip install requests beautifulsoup4 pandas matplotlib openpyxl streamlit

🚀 Running the Project

Step 1: Run Web Scraper

python scraper.py



This will:



Scrape website data

Save files in /data folder

Generate logs in /logs

Step 2: Generate Charts

python chart.py



Chart will be saved in:



charts/chart.png

Step 3: Run Dashboard

python -m streamlit run dashboard.py



Then open:



http://localhost:8501

📊 Output Example



After running the project, you will get:



Data Files

books.csv

books.xlsx

books.db

Logs

scraper.log

Visualization

chart.png

Dashboard

Interactive data filtering system

🧪 Key Functionalities

🔹 Web Scraping



Extracts book data from:



Books to Scrape



🔹 Data Storage



Stores data in:



CSV (for analysis)

Excel (for reporting)

SQLite database (for querying)

🔹 Visualization



Generates bar chart of book ratings distribution.



🔹 Dashboard



Interactive Streamlit interface for:



Viewing dataset

Filtering by rating

Exploring scraped data

⚠️ Troubleshooting

Issue	Solution

Streamlit not found	Run pip install streamlit

No space left error	Free disk storage

CSV not generated	Check scraper logs

Dashboard not opening	Use python -m streamlit run dashboard.py

🧠 Learning Outcomes



This project demonstrates:



Web scraping fundamentals

Data engineering pipeline

File handling in Python

Database integration (SQLite)

Data visualization

Dashboard development

Real-world automation workflow

