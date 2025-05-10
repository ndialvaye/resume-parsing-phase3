import streamlit as st
from utils import extract_named_entities, display_entities


st.title("🧠 Resume Parsing - Phase 3: Named Entity Recognition")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Résumé uploaded successfully. Extracting entities...")

    entities = extract_named_entities("temp_resume.pdf")
    display_entities(entities)
