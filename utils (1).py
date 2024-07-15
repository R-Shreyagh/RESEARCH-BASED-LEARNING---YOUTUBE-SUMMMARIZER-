from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

def summarize_text(text):
    summarizer = pipeline('summarization')
    num_iters = len(text) // 1000
    summarized_text = []
    
    for i in range(num_iters + 1):
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(text[start:end])[0]['summary_text']
        summarized_text.append(out)
    
    return summarized_text
