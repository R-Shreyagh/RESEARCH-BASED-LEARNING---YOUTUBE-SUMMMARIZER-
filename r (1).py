import streamlit as st
import re
from utils import fetch_transcript, summarize_text

def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    Handles various YouTube URL formats.
    """
    video_id = None
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            video_id = match.group(1)
            break
    return video_id

def main():
    st.title("YouTube Video Summarizer")
    
    youtube_video = st.text_input("Enter YouTube video URL", "")
    
    if st.button("Summarize"):
        if youtube_video:
            video_id = extract_video_id(youtube_video)
            if video_id:
                with st.spinner("Fetching transcript..."):
                    try:
                        transcript = fetch_transcript(video_id)
                        result = " ".join([i['text'] for i in transcript])
                    except Exception as e:
                        st.error(f"Error fetching transcript: {e}")
                        return
                
                with st.spinner("Summarizing text..."):
                    try:
                        summarized_text = summarize_text(result)
                        for summary in summarized_text:
                            st.write(summary)
                    except Exception as e:
                        st.error(f"Error summarizing text: {e}")
            else:
                st.warning("Invalid YouTube URL. Please enter a valid YouTube video URL.")
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    main()
