
import spacy
import streamlit as st

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def display_entities(entities):
    if not entities:
        st.warning("Aucune entité trouvée.")
        return
    for text, label in entities:
        st.markdown(f"**{label}**: {text}")
