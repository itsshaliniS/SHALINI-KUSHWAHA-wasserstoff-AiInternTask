
import faiss
import numpy as np
import pickle
import os

class FAISSIndex:
    def __init__(self, dim=384, db_path="faiss_index/index"):
        self.dim = dim
        self.db_path = db_path
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings).astype("float32"))
        self.text_chunks.extend(chunks)

    def save(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        faiss.write_index(self.index, f"{self.db_path}.index")
        with open(f"{self.db_path}.pkl", "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load(self):
        self.index = faiss.read_index(f"{self.db_path}.index")
        with open(f"{self.db_path}.pkl", "rb") as f:
            self.text_chunks = pickle.load(f)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]).astype("float32"), top_k)
        return [(self.text_chunks[i], float(D[0][j])) for j, i in enumerate(I[0])]
