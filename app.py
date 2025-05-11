
import streamlit as st
from utils import extract_named_entities, display_entities

st.title("Analyse des entités nommées dans les CVs")

uploaded_file = st.file_uploader("Téléversez un CV au format PDF", type="pdf")

if uploaded_file:
    with st.spinner("Traitement en cours..."):
        entities = extract_named_entities(uploaded_file)
        display_entities(entities)
