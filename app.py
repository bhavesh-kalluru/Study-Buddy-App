import streamlit as st
from dotenv import load_dotenv
import os

from pdf_handler import extract_text_from_pdf
from utils import summarize_text, explain_text, generate_quiz
from word_converter import convert_pdf_to_docx

# Load environment variables
load_dotenv()

st.set_page_config(page_title="📚 StudyBuddy AI", layout="wide")
st.title("📚 StudyBuddy AI - Your Study Companion")

# Template Selector
template = st.selectbox("🖋️ Choose Template Style", ["Simple", "Detailed", "Bullet Points"])

# PDF Upload
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("temp.pdf")

    st.subheader("Choose an action:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📄 Summarize"):
            summary = summarize_text(text, template)
            st.success("Summary:")
            st.write(summary)

    with col2:
        if st.button("🧠 Explain"):
            explanation = explain_text(text, template)
            st.info("Explanation:")
            st.write(explanation)

    with col3:
        if st.button("❓ Generate Quiz"):
            quiz = generate_quiz(text, template)
            st.warning("Quiz Questions:")
            st.write(quiz)

    with col4:
        if st.button("📤 Convert to Word"):
            docx_path = convert_pdf_to_docx("temp.pdf")
            with open(docx_path, "rb") as docx_file:
                st.download_button("Download .docx", docx_file, file_name="converted.docx")
