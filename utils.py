
import spacy
import PyPDF2
import streamlit as st

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    if not entities:
        st.warning("Aucune entité trouvée.")
    else:
        st.write("### 📌 Entités reconnues")
        for entity, label in entities:
            st.markdown(f"• **{label}**: {entity}")
