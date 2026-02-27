# llm.py

import ollama

def generate_response(prompt):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a helpful AI research assistant."},
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0.3}
    )

    return response["message"]["content"]