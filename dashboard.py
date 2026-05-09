import streamlit as st
import pandas as pd

df = pd.read_csv("books.csv")

st.title("Book Scraping Dashboard")

st.dataframe(df)

rating = st.selectbox(
    "Filter by Rating",
    df["Rating"].unique()
)

filtered = df[df["Rating"] == rating]

st.write(filtered)