# embedding_engine.py

import ollama
import numpy as np

def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return np.array(response["embedding"])


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_relevant_chunks(chunks, question, top_k=3):

    question_embedding = get_embedding(question)

    scored = []

    for chunk in chunks:
        chunk_embedding = get_embedding(chunk)
        score = cosine_similarity(question_embedding, chunk_embedding)
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [chunk for score, chunk in scored[:top_k]]