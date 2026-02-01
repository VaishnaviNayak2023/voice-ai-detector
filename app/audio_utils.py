import tempfile
import requests
import librosa
import numpy as np


def download_audio(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp.write(response.content)
    tmp.close()
    return tmp.name




def extract_features(path: str) -> np.ndarray:
    y, sr = librosa.load(path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1)