import faiss
import numpy as np
import torch
from sentence_transformers import SentenceTransformer

class RAGRetriever:
    def __init__(self, documents):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)
        self.docs = documents
        self.doc_embeddings = self.model.encode(documents)
        self.index.add(np.array(self.doc_embeddings).astype('float32'))

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query]).astype('float32')
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.docs[idx] for idx in indices[0]]
