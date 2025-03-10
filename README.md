# WhisperAI
Speech-to-Text & Translation App using Whisper

📌 Overview

This Streamlit-based application leverages OpenAI's Whisper model for:

Speech-to-Text transcription of audio files.

Translation of non-English speech into English.

It supports various Whisper models (tiny, medium, large) and accepts mp3, wav, and m4a audio formats.

🎥 Demo

A quick demo of the Speech-to-Text App in action.

🚀 Features

✅ Transcribe Speech: Converts spoken language into text.✅ Translate Speech: Converts non-English speech into English.✅ Multiple Whisper Models: Choose from tiny, medium, or large.✅ User-Friendly Interface: Simple, intuitive design using Streamlit.

🛠️ Installation & Setup

🔹 1. Clone the Repository

git clone https://github.com/your-repo/whisper-stt.git
cd whisper-stt

🔹 2. Install Dependencies

Ensure you have Python 3.8+ installed. Then, run:

pip install -r requirements.txt

🔹 3. Run the Application

streamlit run app.py

📝 Usage Guide

Select a Whisper Model (tiny, medium, large).

Upload an audio file (supports mp3, wav, m4a).

Click Transcribe to convert speech to text.

Click Translate into English for language translation.

View the output text in the Streamlit UI.

📸 Screenshots

🔹 App UI



🔹 Transcription Output



⚙️ Requirements

Python 3.8+

Streamlit

OpenAI Whisper

Pyttsx3

gTTS

pydub

ffmpeg (for audio conversion)

🔧 Troubleshooting

If you get an ffmpeg error, install it using:

sudo apt install ffmpeg  # For Linux
brew install ffmpeg      # For macOS
choco install ffmpeg     # For Windows (Chocolatey)

If Whisper fails to load, try:

pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cu118

🤖 Future Enhancements

🎤 Real-time voice recording & transcription.

🌍 Multi-language support beyond English.

📱 Mobile-friendly UI enhancements.

📬 Contact & Support

For issues or feature requests, reach out via GitHub Issues.

⭐ Like this project? Give it a star on GitHub!
