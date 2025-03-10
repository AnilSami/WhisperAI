#import whisper

#model = whisper.load_model('medium')

#result = model.transcribe("German.mp3")

#print(result['text'])

import whisper

# Step 1: Load the Whisper model
model = whisper.load_model("base")  # Use "tiny", "base", "small", "medium", or "large"

# Step 2: Load and preprocess the audio
audio = whisper.load_audio("German.mp3")
audio = whisper.pad_or_trim(audio)

# Step 3: Create a log-Mel spectrogram
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

# Step 4: Detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# Step 5: Decode the audio into text
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# Step 6: Print the recognized text
print(result.text)