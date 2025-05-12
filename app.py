import streamlit as st
from utils import extract_named_entities, display_entities
import os

st.title("🔍 Resume Parsing - Phase 3: Named Entity Recognition")

uploaded_file = st.file_uploader("Upload a resume (PDF)", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    entities = extract_named_entities("temp.pdf")
    st.subheader("📌 Extracted Entities")
    display_entities(entities)
