
import spacy
from PyPDF2 import PdfReader
import streamlit as st

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    st.subheader("Entités nommées extraites :")
    for ent_text, ent_label in entities:
        st.write(f"**{ent_label}** : {ent_text}")
