import streamlit as st
from utils import extract_named_entities

st.set_page_config(page_title="Resume NER - Phase 3", layout="centered")

st.title("📄 Resume NER - Phase 3")
st.markdown("Upload a PDF resume to extract named entities using spaCy.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_file is not None:
    text, entities = extract_named_entities(uploaded_file)
    st.subheader("Extracted Text")
    st.text(text)

    st.subheader("Named Entities")
    for ent, label in entities:
        st.markdown(f"**{ent}** — `{label}`")