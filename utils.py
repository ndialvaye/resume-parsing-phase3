import spacy
import PyPDF2
import pandas as pd
import streamlit as st

def extract_text_from_pdf(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_named_entities(pdf_path):
    nlp = spacy.load("en_core_web_sm")
    text = extract_text_from_pdf(pdf_path)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    df = pd.DataFrame(entities, columns=["Entity", "Label"])
    st.dataframe(df)
