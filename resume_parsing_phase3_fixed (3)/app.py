
import streamlit as st
from utils import extract_named_entities, display_entities
from PyPDF2 import PdfReader

st.set_page_config(page_title="Phase 3 - NER", layout="centered")
st.title("Phase 3 - Extraction d'entités nommées (NER)")

uploaded_file = st.file_uploader("Téléchargez un CV (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    if text.strip():
        entities = extract_named_entities(text)
        display_entities(entities)
    else:
        st.error("Le fichier PDF est vide ou non lisible.")
