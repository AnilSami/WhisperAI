import streamlit as st
import whisper


# Load the Whisper model
@st.cache_resource  # Cache the model to avoid reloading on every interaction
def load_model():
    return whisper.load_model("base")

# Title of the app
st.title("Whisper AI Speech-to-Text Prototype")

# File uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file:
    # Display the uploaded audio file
    st.audio(audio_file, format="audio/wav")

    # Transcribe the audio file
    if st.button("Transcribe"):
        st.write("Transcribing... Please wait.")
        
        # Load the Whisper model
        model = load_model()
        
        # Save the uploaded file temporarily
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.getbuffer())
        
        # Transcribe the audio
        result = model.transcribe("temp_audio.mp3")
        
        # Display the transcription
        st.write("Transcription:")
        st.write(result["text"])