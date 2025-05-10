
import spacy
from PyPDF2 import PdfReader

# Chargement automatique du modèle en_core_web_sm si non installé
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_named_entities(file_bytes):
    text = ""
    reader = PdfReader(file_bytes)
    for page in reader.pages:
        text += page.extract_text() + "\n"

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def display_entities(entities):
    if not entities:
        st.info("Aucune entité détectée.")
    else:
        for text, label in entities:
            st.markdown(f"**{label}** : {text}")
