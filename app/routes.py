from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import verify_api_key
# We change this to a function that handles strings, not downloads
from app.audio_utils import save_base64_audio 
from app.detector import detect_voice

router = APIRouter()

# This class defines what the "Request Body" must look like
class DetectRequest(BaseModel):
    audio_base64: str    # Changed from HttpUrl to str to accept the long text
    language: str
    audio_format: str = "mp3" # Added to match your tool's input

class DetectResponse(BaseModel):
    classification: str
    confidence: float
    explanation: str

@router.post("/detect", response_model=DetectResponse)
def detect(req: DetectRequest, auth=Depends(verify_api_key)):
    # 1. Save the Base64 string as a temporary file
    audio_path = save_base64_audio(req.audio_base64, req.audio_format)
    
    # 2. Run the detection
    classification, confidence, explanation = detect_voice(audio_path, req.language)

    return {
        "classification": classification,
        "confidence": confidence,
        "explanation": explanation
    }
