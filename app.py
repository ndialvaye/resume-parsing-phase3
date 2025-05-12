import streamlit as st
from utils import extract_named_entities, display_entities

st.title("Phase 3 - Named Entity Recognition (NER) sur les CVs")

uploaded_file = st.file_uploader("Uploader un CV (format PDF)", type="pdf")

if uploaded_file:
    st.success("Fichier bien reçu.")
    text, entities = extract_named_entities(uploaded_file)
    st.subheader("Texte extrait :")
    st.write(text)

    st.subheader("Entités reconnues :")
    display_entities(entities)