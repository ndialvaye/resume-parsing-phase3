import streamlit as st
from utils import extract_named_entities, display_entities

st.title("Extraction d'entités nommées à partir de CVs")

uploaded_file = st.file_uploader("Téléversez un fichier PDF de CV", type=["pdf"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("latin-1")
    entities = extract_named_entities(text)
    display_entities(entities)