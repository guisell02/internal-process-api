from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    """
    User ORM model.

    Represents the 'users' table in the database.

    Fields:
        id: Primary key.
        first_name: User's first name.
        last_name: User's last name.
        email: Unique email address.
        password_hash: Hashed password.
        role_id: Role identifier (FK in future).
        is_active: Indicates if the user is active.
        created_at: Timestamp when the user was created.
        updated_at: Timestamp when the user was last updated.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=True)

    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)

    role_id: Mapped[int] = mapped_column(Integer, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )
