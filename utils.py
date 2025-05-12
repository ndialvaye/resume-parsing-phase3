import spacy
from PyPDF2 import PdfReader
import streamlit as st

# Charger le modèle SpaCy
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(pdf_file):
    text = ""
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text()

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return text, entities

def display_entities(entities):
    for ent, label in entities:
        st.write(f"{ent} ({label})")