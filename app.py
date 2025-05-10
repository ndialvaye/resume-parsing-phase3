
import streamlit as st
from utils import extract_named_entities, display_entities

st.title("📄 Analyse de CV - Phase 3 : Reconnaissance d'entités nommées (NER)")

uploaded_file = st.file_uploader("Uploader un CV (PDF uniquement)", type=["pdf"])

if uploaded_file is not None:
    text = uploaded_file.read()
    named_entities = extract_named_entities(text)
    st.subheader("📌 Entités extraites")
    display_entities(named_entities)
