
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    return model.encode([chunk["chunk"] for chunk in chunks])

def embed_query(query):
    return model.encode([query])[0]
