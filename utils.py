import spacy

# Charger le modèle en_core_web_sm compatible avec spacy==3.5
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    import streamlit as st
    st.subheader("Entités extraites :")
    for ent_text, ent_label in entities:
        st.write(f"{ent_text} → {ent_label}")