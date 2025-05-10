import streamlit as st
from utils import extract_named_entities, display_entities

st.set_page_config(page_title="Phase 3 – NER", layout="centered")

st.title("🔍 Phase 3 – NER : Extraction des Entités Nommées")

st.markdown("""
Cette application extrait automatiquement les entités nommées (nom, organisation, lieux, dates, etc.) à partir de CV (format texte brut).
Elle s'inspire des bonnes pratiques décrites dans :
- [nanonets.com](https://nanonets.com/blog/named-entity-recognition-with-nltk-and-spacy/)
- [bluetickconsultants.com](https://www.bluetickconsultants.com/enity-recognition-on-images-using-ocr.html)
""")

uploaded_files = st.file_uploader("📁 Uploadez un ou plusieurs fichiers .txt contenant du texte extrait de CV", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"📄 Fichier traité : {uploaded_file.name}")
        try:
            text = uploaded_file.read().decode("utf-8")
            entities = extract_named_entities(text)
            display_entities(entities)
        except Exception as e:
            st.error(f"❌ Erreur avec {uploaded_file.name} : {e}")
else:
    st.info("Veuillez uploader un ou plusieurs fichiers texte contenant des CV.")