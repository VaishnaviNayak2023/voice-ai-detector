from fastapi import Header, HTTPException
from app.config import API_KEY


def verify_api_key(authorization: str = Header(...)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
