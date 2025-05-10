import spacy
import pandas as pd
import streamlit as st

# Chargement robuste du modèle SpaCy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    data = {"Texte": [], "Étiquette": []}
    for ent in doc.ents:
        data["Texte"].append(ent.text)
        data["Étiquette"].append(ent.label_)
    return pd.DataFrame(data)

def display_entities(df):
    if not df.empty:
        st.dataframe(df)
        st.download_button("📥 Télécharger en CSV", df.to_csv(index=False).encode(), "entites_nommes.csv")
    else:
        st.warning("Aucune entité trouvée.")