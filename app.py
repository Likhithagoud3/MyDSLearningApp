import streamlit as st

st.title("📚 Learn Data Science App by Likhitha")

st.header("🐍 Python Basics - Cheat Sheet")

try:
    with open("python_cheat.txt", "r", encoding="utf-8") as file:
        cheat_content = file.read()
    st.text_area("📘 Python Cheat Code", cheat_content, height=400)
except FileNotFoundError:
    st.error("❌ Cheat code file not found. Please upload 'python_cheat.txt' to your GitHub repo.")



