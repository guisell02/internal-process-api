from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

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

    def __init__(self, db: Session):
        """
        Initialize service with a shared database session.

        Args:
            db (Session): Active SQLAlchemy session.
        """
        self.db = db
        self.user_repository = UserRepository(db)

    def create_user(self, user_data: dict) -> User:
        """
        Create a new user.

        Workflow:
        1. Validate business rules.
        2. Create ORM entity.
        3. Persist entity using repository.
        4. Commit transaction.

        Args:
            user_data (dict): User input data.

        Returns:
            User: Newly created user.

        Raises:
            UserAlreadyExistsError:
                If a user with the same email already exists.
        """
        try:
            # Validate unique email
            existing_user = self.user_repository.get_user_by_email(user_data["email"])

            if existing_user:
                raise UserAlreadyExistsError()

            # Create ORM entity
            user = User(**user_data)

            # Persist entity
            self.user_repository.create_user(user)

            # Commit transaction
            self.db.commit()

            return user

        except IntegrityError:
            self.db.rollback()

            # Handles race conditions / DB unique constraint violations
            raise UserAlreadyExistsError()

        except Exception:
            self.db.rollback()
            raise
