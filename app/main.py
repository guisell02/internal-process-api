from fastapi import FastAPI

from app.core.config import PROJECT_NAME
from app.database.base import Base
from app.database.engine import engine
from app.exceptions.handlers import register_exception_handlers
from app.routers.users import user_router

# IMPORTANT

app = FastAPI(title=PROJECT_NAME)

Base.metadata.create_all(bind=engine)

# Registering or Binding handlers
register_exception_handlers(app)

# Router user

app.include_router(user_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
