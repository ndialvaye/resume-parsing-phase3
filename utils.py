import re
import spacy
from PyPDF2 import PdfReader
import streamlit as st

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        st.error(f"Erreur de lecture du PDF : {e}")
    return text

def extract_named_entities(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    doc = nlp(text)
    entities = [(ent.text.strip(), ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    if not entities:
        st.warning("Aucune entité trouvée.")
        return
    labels = sorted(set(label for _, label in entities))
    for label in labels:
        st.subheader(label)
        items = [text for text, lbl in entities if lbl == label]
        st.write(", ".join(set(items)))
