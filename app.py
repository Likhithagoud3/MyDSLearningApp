import streamlit as st
from docx import Document

st.title("📚 Learn Data Science App by Likitha")
st.header("📄 Data Types, Central Tendency & Dispersion")

def read_docx(file_path):
    doc = Document(file_path)
    content = ""
    for para in doc.paragraphs:
        content += para.text + "\n"
    return content

try:
    doc_text = read_docx("Data_Types_Central_Tendency_Dispersion(1).docx")  # use exact name
    st.text_area("Document Content", doc_text, height=600)
except Exception as e:
    st.error(f"⚠ Could not load the DOCX file: {e}")



