
import streamlit as st
from utils import extract_named_entities, display_entities

st.set_page_config(page_title="Phase 3 - Named Entity Recognition", layout="wide")

st.title("🔍 Phase 3 - Extraction d'entités nommées (NER)")

uploaded_file = st.file_uploader("📄 Choisissez un fichier PDF", type="pdf")

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    with st.spinner("⏳ Extraction des entités..."):
        entities = extract_named_entities("temp_resume.pdf")
    st.success("✅ Extraction terminée !")
    display_entities(entities)
