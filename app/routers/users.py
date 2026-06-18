from fastapi import APIRouter, Depends

from app.api.dependencies.dependencies import get_user_service
from app.schemas.user_schemas import CreateUserSchema, UserResponseSchema
from app.services.user_service import UserService

user_router = APIRouter()


@user_router.post(
    "/users",
    response_model=UserResponseSchema,
    responses={409: {"description": "user already exists"}},
)
def create_user(
    data: CreateUserSchema, service: UserService = Depends(get_user_service)
) -> UserResponseSchema:
    user = service.create_user(data)
    return user
