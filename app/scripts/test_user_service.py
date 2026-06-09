"""
Manual integration test for UserService.

This script validates the complete user creation workflow:

CreateUserSchema
→ UserService
→ UserRepository
→ Database

Not part of production code.
"""

import logging

from app.database.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import CreateUserSchema
from app.services.user_service import UserService
from app.exceptions.user_exceptions import UserAlreadyExistsError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Execute manual UserService integration test.
    """
    user_data = CreateUserSchema(
        first_name="Ana",
        last_name="Perez",
        email="anaperez@example.com",
        password="12345678",
    )

    db = SessionLocal()
    user_repository = UserRepository(db)
    user_service = UserService(
        db=db,
        user_repository=user_repository,
    )

    try:

        logger.info("Testing successful user creation")
        created_user = user_service.create_user(user_data)
        logger.info(f"User successfully created with ID: {created_user.id}")

        logger.info("Testing duplicate email validation")

        try:
            created_user = user_service.create_user(user_data)

        except UserAlreadyExistsError as e:
            logger.error(f"user duplicated {e}")

    except Exception as e:
        logger.info("The service protected the database.")
        logger.error(f"Error during user creation: {e}")

    finally:
        db.close()
        logger.info("Database session closed")


if __name__ == "__main__":
    main()
