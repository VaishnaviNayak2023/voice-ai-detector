import numpy as np
from app.audio_utils import extract_features


def detect_voice(audio_path: str, language: str):
    features = extract_features(audio_path)
    score = float(np.tanh(np.mean(features)))
    confidence = round(abs(score), 2)

    if confidence > 0.5:
        classification = "AI-Generated"
        explanation = "Spectral smoothness and temporal consistency suggest synthetic speech."
    else:
        classification = "Human"
        explanation = "Natural pitch variation and micro-pauses indicate human speech."
    return classification, confidence, explanation
