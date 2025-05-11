
import streamlit as st
from utils import extract_text_from_pdf, extract_named_entities
import pandas as pd

st.title("Extraction des Entités Nommées depuis un CV")

uploaded_file = st.file_uploader("Téléchargez un fichier PDF", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Texte extrait :")
    st.write(text[:1000] + "...")
    
    entities = extract_named_entities(text)
    st.subheader("Entités Nommées :")
    st.dataframe(pd.DataFrame(entities, columns=["Entité", "Type"]))
