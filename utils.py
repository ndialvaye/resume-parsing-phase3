
import spacy
from PyPDF2 import PdfReader
import pandas as pd
import streamlit as st
import io

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(uploaded_pdf):
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    doc = nlp(text)
    data = [(ent.text, ent.label_) for ent in doc.ents]
    return data

def display_entities(entities):
    if not entities:
        st.warning("Aucune entité nommée détectée.")
        return
    df = pd.DataFrame(entities, columns=["Texte", "Type d'entité"])
    st.write(df)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Entités")
    st.download_button(
        label="Télécharger les entités en Excel",
        data=output.getvalue(),
        file_name="entites_nommes.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
