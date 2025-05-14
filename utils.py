import spacy
import PyPDF2

def extract_named_entities(uploaded_file):
    pdf = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return text, entities
