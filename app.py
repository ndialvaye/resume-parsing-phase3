import streamlit as st
from utils import extract_named_entities, display_entities

st.set_page_config(page_title="Phase 3 – NER", layout="centered")

st.title("🔍 Phase 3 – Extraction des Entités Nommées (NER)")

st.markdown("""
Cette application permet d'extraire automatiquement les entités nommées (nom, organisation, lieux, dates, etc.)
à partir de CV en texte brut.
""")

uploaded_files = st.file_uploader("📁 Uploader un ou plusieurs fichiers .txt", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            text = uploaded_file.read().decode("utf-8")
            st.subheader(f"📄 Résultat pour : {uploaded_file.name}")
            entities = extract_named_entities(text)
            display_entities(entities)
        except Exception as e:
            st.error(f"❌ Une erreur est survenue pour {uploaded_file.name} : {e}")
else:
    st.info("Veuillez uploader au moins un fichier texte pour commencer.")