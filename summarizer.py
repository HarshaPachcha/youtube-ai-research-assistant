# summarizer.py

from llm import generate_response

def generate_summary(transcript_data, language="English"):

    full_text = ""
    for entry in transcript_data:
        full_text += f"[{entry['start']} sec] {entry['text']} "

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
    You are a professional YouTube research assistant.

    {lang_instruction}

    Provide:

    🎥 Video Title
    📌 5 Key Points (with timestamps)
    ⏱ 3 Most Important Moments (accurate timestamps)
    🧠 Core Business Insight

    Use timestamps exactly as provided.
    Do not invent timestamps.

    Transcript:
    {full_text[:12000]}
    """

    return generate_response(prompt)