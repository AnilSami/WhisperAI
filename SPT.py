import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as F
import torch.nn as nn

# Load an audio file
audio_file = audio_file = "C:\\Users\\anils\\Whisper\\od\\share\\Solo_Audio_1.mp3"
y, sr = librosa.load(audio_file, sr=16000)  # Load with 16kHz sampling rate

# Compute Short-Time Fourier Transform (STFT)
spectrogram = np.abs(librosa.stft(y, n_fft=512, hop_length=256))

# Display the Spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), 
                         sr=sr, hop_length=256, cmap='coolwarm', y_axis='log', x_axis='time')
plt.title("Spectrogram Matrix")
plt.colorbar(format="%+2.0f dB")
plt.show()

# Print matrix shape
#print("Spectrogram Matrix Shape:", spectrogram.shape)  # Example: (257, Time_Frames)


# Convert Spectrogram to Mel-Spectrogram (Whisper uses Mel features)
mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

# Convert to decibels
mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

# Display the Mel-Spectrogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel', cmap='coolwarm')
plt.title("Mel-Spectrogram (Feature Matrix)")
plt.colorbar(format="%+2.0f dB")
plt.show()

# Print matrix shape
#print("Feature Matrix Shape:", mel_spectrogram.shape)  # Example: (128, Time_Frames)






# Define a simple Transformer Encoder Layer (used in Whisper)
encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)

# Dummy input tensor (Feature matrix: 128 features over 100 time frames)
feature_matrix = torch.rand(100, 1, 512)  # Shape: (Time_Frames, Batch_Size, Feature_Size)

# Forward pass through Transformer
output = transformer_encoder(feature_matrix)

# Print output matrix shape
print("Transformer Output Matrix Shape:", output.shape)  # Example: (100, 1, 512)







# Dummy output from Transformer (100 time steps, vocabulary size of 50,000)
vocab_size = 50000
logits = torch.rand(100, vocab_size)  # Random scores for words

# Apply Softmax to get probabilities
prob_matrix = F.softmax(logits, dim=1)

# Print matrix shape and example probabilities
print("Output Probability Matrix Shape:", prob_matrix.shape)  # Example: (100, 50000)
print("Sample Probabilities for First Time Step:", prob_matrix[0][:5])  # Show top 5 word probabilities

