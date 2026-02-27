# qa_engine.py

from llm import generate_response
from embedding_engine import retrieve_relevant_chunks

def answer_question(chunks, question, language="English"):

    relevant_chunks = retrieve_relevant_chunks(chunks, question)
    context = "\n\n".join(relevant_chunks)

    if language.lower() == "hindi":
        lang_instruction = (
            "IMPORTANT: The entire response must be written ONLY in Hindi. "
            "Do not use English."
        )
    else:
        lang_instruction = (
            "IMPORTANT: The entire response must be written ONLY in English."
        )

    prompt = f"""
    You are a YouTube AI assistant.

    {lang_instruction}

    Answer strictly using the context below.
    If the answer is not present, reply:
    "This topic is not covered in the video."

    Context:
    {context}

    Question:
    {question}
    """

    return generate_response(prompt)