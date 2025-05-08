import streamlit as st
from utils import extract_named_entities, display_entities
import os

st.title("🔍 Phase 3 – Extraction des Entités Nommées (NER)")
uploaded_files = st.file_uploader("Uploader un ou plusieurs CV (.txt)", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        text = uploaded_file.read().decode("utf-8")
        st.subheader(f"📄 Résultat pour : {uploaded_file.name}")
        entities = extract_named_entities(text)
        display_entities(entities)