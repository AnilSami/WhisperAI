import streamlit as st
import whisper
import pyttsx3
from gtts import gTTS
import os
from pydub import AudioSegment

st.title("Speech-to-Text Converter")
st.title("Whisper can translate only other languages into English")

def transcribe_audio(model_type, audio_file):
    if audio_file is None:
        return "Please upload an audio file."

    model = whisper.load_model(model_type)
    result = model.transcribe(audio_file.name)  
    st.write(audio_file.name)
    return result["text"]

def translate_audio(model_type, audio_file):
    if audio_file is None:
        return "Please upload an audio file."

    model = whisper.load_model(model_type)
    result = model.transcribe(audio_file.name, task="translate")  
    return result["text"]



model_type = st.selectbox("Select Whisper model:", ["tiny", "medium", "large"])
audio_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a"])



if st.button("Transcribe"):
    text = transcribe_audio(model_type, audio_file)
    st.write("Transcribed Text:")
    st.write(text)

elif st.button("Translate into English"):
    text = translate_audio(model_type, audio_file)
    st.write("Translated Text into English:")
    st.write(text)