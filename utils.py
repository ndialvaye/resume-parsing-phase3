import spacy
import pandas as pd
import PyPDF2
from io import BytesIO

# Charger le modèle NER de spaCy
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(pdf_file):
    reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    doc = nlp(text)
    data = [(ent.text, ent.label_) for ent in doc.ents]
    df = pd.DataFrame(data, columns=["Texte", "Type"]) if data else pd.DataFrame()
    return df