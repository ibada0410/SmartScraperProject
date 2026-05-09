import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import logging
import time
import os

# ---------- CREATE FOLDERS SAFELY ----------
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

# ---------- LOGGING SETUP ----------
logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

headers = {"User-Agent": "Mozilla/5.0"}

data = []

# ---------- SCRAPING ----------
for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            availability = book.find("p", class_="instock availability").text.strip()

            image = "https://books.toscrape.com/" + book.find("img")["src"]

            data.append([title, price, rating, availability, image])

        logging.info(f"Page {page} scraped successfully")
        print(f"Page {page} scraped")

        time.sleep(2)

    except Exception as e:
        logging.error(f"Error on page {page}: {e}")

# ---------- DATAFRAME ----------
df = pd.DataFrame(data, columns=[
    "Title", "Price", "Rating", "Availability", "Image_URL"
])

df["Price"] = df["Price"].str.replace("£", "")

# ---------- SAVE FILES IN DATA FOLDER ----------
csv_path = "data/books.csv"
excel_path = "data/books.xlsx"
db_path = "data/books.db"

df.to_csv(csv_path, index=False)
df.to_excel(excel_path, index=False)

conn = sqlite3.connect(db_path)
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()

print("\nPROJECT COMPLETED SUCCESSFULLY")