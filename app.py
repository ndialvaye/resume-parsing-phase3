import streamlit as st
from utils import extract_named_entities
import pandas as pd
import spacy

st.set_page_config(page_title="Resume NER Parser - Phase 3")

st.title("📄 Résumé NER Parser - Phase 3")

uploaded_file = st.file_uploader("Téléversez un fichier PDF de CV", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyse en cours..."):
        text, entities = extract_named_entities(uploaded_file)

        st.subheader("Texte extrait")
        st.write(text[:1000] + "..." if len(text) > 1000 else text)

        st.subheader("Entités reconnues")
        df = pd.DataFrame(entities, columns=["Texte", "Label"])
        st.dataframe(df)
