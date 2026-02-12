from fastapi import FastAPI
from app.core.config import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME)

@app.get("/health")
def health_check():
    return {"status": "ok"}