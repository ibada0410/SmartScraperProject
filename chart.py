import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/books.csv")

rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8,5))
rating_counts.plot(kind="bar")

plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")

plt.savefig("charts/chart.png")   # ✅ SAVED HERE

plt.show()