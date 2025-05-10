
import streamlit as st
from utils import extract_named_entities, display_entities

st.title("Phase 3 : Reconnaissance d'entités nommées (NER)")

uploaded_file = st.file_uploader("Téléverser un CV au format PDF", type=["pdf"])
if uploaded_file is not None:
    with open("uploaded_cv.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("Fichier chargé avec succès.")
    entities = extract_named_entities("uploaded_cv.pdf")
    display_entities(entities)
