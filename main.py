import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("img.jpeg")

with col2:
    st.title("Capătă Ciprian")
    content = """
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
     Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
     Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    """
    st.info(content)
content2 = """
Below I have attached some of my Python projects. Feel free to contact me.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(Image.open("imgs/" + row['image']))
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(Image.open("imgs/" + row['image']))
        st.write(f"[Source Code]({row['url']})")
