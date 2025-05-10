import streamlit as st
from utils import extract_named_entities, display_entities

st.set_page_config(page_title="Resume NER", layout="centered")

st.title("📄 Extraction des entités depuis un CV (Phase 3)")

uploaded_file = st.file_uploader("Téléversez un fichier PDF de CV", type=["pdf"])

if uploaded_file is not None:
    st.success("📥 Fichier chargé avec succès. Traitement en cours...")
    entities = extract_named_entities(uploaded_file)
    st.subheader("📌 Résultat de l'extraction des entités :")
    display_entities(entities)