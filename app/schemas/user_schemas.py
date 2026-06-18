"""
Pydantic schemas for user-related API operations.

These schemas are responsible for:
- Request validation
- Response serialization
- API data contracts
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class CreateUserSchema(BaseModel):
    """
    Schema used to validate user creation requests.

    Required fields:
    - first_name
    - last_name
    - email
    - password
    """

    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UpdateUserSchema(BaseModel):
    """
    Schema used to validate partial user updates.

    All fields are optional to allow partial updates.
    """

    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class UserResponseSchema(BaseModel):
    """
    Schema used for user responses returned to API clients.

    Sensitive fields such as password_hash are intentionally excluded.
    """

    id: int
    first_name: str
    last_name: str | None
    email: EmailStr
    role_id: int | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
