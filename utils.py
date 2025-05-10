import re
import fitz  # PyMuPDF
import spacy

import streamlit as st

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_named_entities(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    text = re.sub(r"\n+", " ", text)
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

def display_entities(entities):
    if not entities:
        st.warning("Aucune entité détectée.")
    else:
        st.write("### ✨ Entités reconnues :")
        for text, label in entities:
            st.markdown(f"**{label}** → {text}")
