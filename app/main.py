from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="AI Voice Detection API")


app.include_router(router, prefix="/api/v1")


@app.get("/")
def health():
    return {"status": "running"}