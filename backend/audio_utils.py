import whisper
import librosa
import numpy as np

# Use a larger model for better accuracy
model = whisper.load_model("medium")

def transcribe_audio(audio_path: str) -> str:
    # Load and normalize audio before transcription
    y, sr = librosa.load(audio_path, sr=16000)
    y = y / np.max(np.abs(y))
    
    result = model.transcribe(y)
    return result["text"]
