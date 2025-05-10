import streamlit as st
from utils import extract_named_entities, display_entities

st.set_page_config(page_title="Resume Parsing Phase 3", layout="wide")

st.title("Phase 3 - Named Entity Recognition (NER)")
st.markdown("Cette application extrait automatiquement les entités nommées des CVs (noms, emails, adresses, compétences, etc.).")

uploaded_file = st.file_uploader("📄 Uploadez un fichier PDF", type=["pdf"])

if uploaded_file:
    with open("temp_cv.pdf", "wb") as f:
        f.write(uploaded_file.read())

    entities = extract_named_entities("temp_cv.pdf")
    st.success("✅ Entités extraites avec succès !")
    display_entities(entities)
