from fastapi import FastAPI
from app.core.config import PROJECT_NAME

from app.database.base import Base
from app.database.engine import engine

# IMPORTANT

app = FastAPI(title=PROJECT_NAME)

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}
