# rag_engine.py

def chunk_transcript(transcript_data, chunk_size=400):

    chunks = []
    current_chunk = ""
    word_count = 0

    for entry in transcript_data:
        line = f"[{entry['start']} sec] {entry['text']} "
        words = line.split()

        if word_count + len(words) > chunk_size:
            chunks.append(current_chunk)
            current_chunk = line
            word_count = len(words)
        else:
            current_chunk += line
            word_count += len(words)

    if current_chunk:
        chunks.append(current_chunk)

    return chunks