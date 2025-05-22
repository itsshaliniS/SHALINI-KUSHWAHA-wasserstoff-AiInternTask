
import streamlit as st
from utils.document_loader import extract_text_from_pdf, extract_text_from_image, save_uploaded_file
from utils.text_splitter import split_text
from utils.embedder import embed_chunks
from utils.vector_store import FAISSIndex
from utils.query_handler import handle_query, cluster_themes, synthesize_themes

st.set_page_config(page_title="GenAI Research Bot", layout="wide")
st.title("Gen-AI Internship Chatbot")


uploaded_files = st.file_uploader("Upload PDFs/Images", type=["pdf", "png", "jpg"], accept_multiple_files=True)

if uploaded_files:
    all_chunks = []
    for file in uploaded_files:
        path = save_uploaded_file(file)
        st.success(f"Uploaded: {file.name}")

        try:
            text = extract_text_from_pdf(path) if file.name.endswith(".pdf") else extract_text_from_image(path)
        except Exception as e:
            st.error(f"Failed to extract text: {e}")

        chunks = split_text(text, filename=file.name)
        all_chunks.extend(chunks)


    st.subheader("Uploaded Files")
    for file in uploaded_files:
        st.markdown(f"- `{file.name}`")

    st.info("Embedding and indexing documents...")
    embeddings = embed_chunks(all_chunks)
    index = FAISSIndex()
    index.add(embeddings, all_chunks)
    index.save()
    st.success("Index created!")


st.header("Ask a Question ")
query = st.text_input("Type your question below:")

if query:
    index = FAISSIndex()
    index.load()
    results = handle_query(index, query)

    st.subheader("Top Results")
    for i, (res, score) in enumerate(results):
        st.markdown(f"**Result {i+1}** — Score: {score:.4f}")
        st.markdown(f"*{res['meta']}*")
        st.markdown(f"> {res['chunk'][:300]}...")

    st.subheader("Themes Across Documents")
    themes = cluster_themes(results)
    summaries = synthesize_themes(themes)
    for label, content in summaries.items():
        st.markdown(f"### Theme {label + 1}")
        st.markdown(f"{content['summary']} ...")
        st.markdown(f"Documents: {', '.join(content['docs'])}")
