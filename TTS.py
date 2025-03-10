import streamlit as st
import whisper
from google.cloud import texttospeech
import os

st.title("Speech-to-Text & Text-to-Speech Converter")

# Load Whisper model (Choose: tiny, base, small, medium, large)
model_type = st.selectbox("Select Whisper model:", ["tiny", "small", "medium", "large"])

# File uploader for audio input
audio_file = st.file_uploader("Upload an Audio File (MP3/WAV/M4A)", type=["mp3", "wav", "m4a"])

# Function: Speech-to-Text using Whisper
def transcribe_audio(model_type, audio_file):
    if audio_file is None:
        return "Please upload an audio file."

    # Load Whisper Model
    model = whisper.load_model(model_type)

    # Save uploaded file locally
    audio_path = "uploaded_audio." + audio_file.name.split(".")[-1]
    with open(audio_path, "wb") as f:
        f.write(audio_file.read())

    # Transcribe audio
    result = model.transcribe(audio_path)
    
    return result["text"]

# Transcription Button
if st.button("Transcribe Audio"):
    text_output = transcribe_audio(model_type, audio_file)
    st.write("Transcribed Text:")
    st.write(text_output)


# Text-to-Speech Section
st.header("Text-to-Speech (Google WaveNet)")

# Input text for TTS
text_input = st.text_area("Enter text to convert into speech:")

# Function: Convert Text to Speech using Google WaveNet
def text_to_speech_wavenet(text):
    if not text:
        return "Please enter text for speech synthesis."

    # Initialize Google Cloud TTS client
    client = texttospeech.TextToSpeechClient()

    # Configure the text input
    text_input = texttospeech.SynthesisInput(text=text)

    # Choose WaveNet voice model
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    # Configure audio output
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Generate speech
    response = client.synthesize_speech(input=text_input, voice=voice, audio_config=audio_config)

    # Save audio file
    output_file = "output_wavenet.mp3"
    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    return output_file

# Button to Convert Text to Speech
if st.button("Convert to Speech"):
    audio_output = text_to_speech_wavenet(text_input)
    st.audio(audio_output, format="audio/mp3")
    st.write("Speech saved as:", audio_output)
