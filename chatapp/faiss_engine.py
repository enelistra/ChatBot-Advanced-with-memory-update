import faiss
import numpy as np
from .nlp import embed

VECTOR_PATH = "data/vectors/"


def split_text(text, size=400, overlap=50):

    words = text.split()
    chunks = []

    for i in range(0, len(words), size - overlap):
        chunk = " ".join(words[i:i+size])
        chunks.append(chunk)

    return chunks


def build_index(company_code, text):

    chunks = split_text(text)

    vectors = embed(chunks)

    dim = vectors.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))

    faiss.write_index(index, f"{VECTOR_PATH}{company_code}.index")

    with open(f"{VECTOR_PATH}{company_code}_chunks.txt", "w", encoding="utf8") as f:
        for c in chunks:
            f.write(c + "\n---\n")


def search(company_code, question, k=3):

    index = faiss.read_index(f"{VECTOR_PATH}{company_code}.index")

    with open(f"{VECTOR_PATH}{company_code}_chunks.txt", encoding="utf8") as f:
        chunks = f.read().split("\n---\n")

    q_vec = embed([question])

    D, I = index.search(np.array(q_vec), k)

    return [chunks[i] for i in I[0]]
