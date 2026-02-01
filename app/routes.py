from fastapi import APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from app.auth import verify_api_key
from app.audio_utils import download_audio
from app.detector import detect_voice


router = APIRouter()


class DetectRequest(BaseModel):
    audio_url: HttpUrl
    language: str
    message: str | None = None


class DetectResponse(BaseModel):
    classification: str
    confidence: float
    explanation: str


@router.post("/detect", response_model=DetectResponse)
def detect(req: DetectRequest, auth=Depends(verify_api_key)):
    audio_path = download_audio(req.audio_url)
    classification, confidence, explanation = detect_voice(audio_path, req.language)


    return {
    "classification": classification,
    "confidence": confidence,
    "explanation": explanation
    }
