import spacy
from PyPDF2 import PdfReader
import streamlit as st

# Charger le modèle de langue
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Le modèle SpaCy 'en_core_web_sm' n'est pas installé.")
    st.stop()

def extract_named_entities(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def display_entities(entities):
    if entities:
        for ent_text, ent_label in entities:
            st.write(f"**{ent_label}** ➤ {ent_text}")
    else:
        st.warning("Aucune entité détectée.")