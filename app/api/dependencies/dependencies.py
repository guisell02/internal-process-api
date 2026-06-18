"Here is an space for to create tools that make part of architecture"

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


def get_db():
    "deliver a session"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Session = Depends(get_db)):
    "Build a repository"
    repository = UserRepository(db)
    return repository


def get_user_service(
    db: Session = Depends(get_db),
    user_repository: UserRepository = Depends(get_user_repository),
):
    "Build a User_Service"
    user_service = UserService(db, user_repository)
    return user_service
