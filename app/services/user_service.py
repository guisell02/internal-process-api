from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.schemas.user_schemas import CreateUserSchema
from app.core.security.password import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.exceptions.user_exceptions import (
    UserAlreadyExistsError,
)


class UserService:
    """
    Service layer responsible for user business logic.

    Responsibilities:
    - Business validations
    - Transaction management
    - Coordinating repositories
    - Translating technical errors into domain exceptions
    """

    def __init__(self, db: Session, user_repository: UserRepository):
        """
        Initialize service with a shared database session.

        Args:
            db (Session): Active SQLAlchemy session.
            user_repository (UserRepository):
                Repository responsible for user persistence operations.
        """
        self.db = db
        self.user_repository = user_repository

    def create_user(self, user_data: CreateUserSchema) -> User:
        """
        Create a new user.

        Workflow:

        1. Validate business rules.
        2. Hash password
        3. Create entity User
        4. Persist entity using repository.
        5. Commit transaction.
        6. Return User

        Args:
            user_data (CreateUserSchema): Validated user creation data

        Returns:
            User: Newly created user.

        Raises:
            UserAlreadyExistsError:
                If a user with the same email already exists.
        """
        message = f"User with email {user_data.email} already exists."

        # Validate unique email
        existing_user = self.user_repository.get_user_by_email(user_data.email)

        if existing_user:
            raise UserAlreadyExistsError(message)

        try:
            # Hashed password
            hashed_password = hash_password(user_data.password)

            # Create ORM entity
            user = User(
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                email=user_data.email,
                password_hash=hashed_password,
            )

            # Persist entity
            self.user_repository.create_user(user)

            # Commit transaction
            self.db.commit()

            return user

        except IntegrityError:
            self.db.rollback()

            # Handles race conditions / DB unique constraint violations
            raise UserAlreadyExistsError(message)

        except Exception:
            self.db.rollback()
            raise
