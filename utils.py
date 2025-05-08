import spacy
import pandas as pd
import streamlit as st

# Télécharger le modèle si besoin
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    data = {"Text": [], "Label": []}
    for ent in doc.ents:
        data["Text"].append(ent.text)
        data["Label"].append(ent.label_)
    return pd.DataFrame(data)

def display_entities(df):
    if not df.empty:
        st.dataframe(df)
        st.download_button("📥 Télécharger les entités en Excel", df.to_csv(index=False).encode(), "entities.csv")
    else:
        st.warning("Aucune entité trouvée.")
