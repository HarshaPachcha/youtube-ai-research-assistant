# transcript.py

from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None


def get_transcript(url):
    try:
        video_id = extract_video_id(url)
        if not video_id:
            return None

        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)

        structured = []
        for entry in fetched:
            structured.append({
                "text": entry.text,
                "start": int(entry.start)
            })

        return structured

    except Exception as e:
        print("Transcript error:", e)
        return None