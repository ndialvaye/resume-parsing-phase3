import streamlit as st
from utils import extract_named_entities

st.set_page_config(page_title="NER Resume Parser", layout="centered")

st.title("🔍 Resume NER Parser")
st.write("Upload a resume in PDF format to extract named entities like name, location, organization, etc.")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Processing..."):
        entities_df = extract_named_entities(uploaded_file)
        if not entities_df.empty:
            st.success("Extraction réussie ! Voici les entités nommées extraites :")
            st.dataframe(entities_df)
        else:
            st.warning("Aucune entité nommée trouvée dans ce document.")