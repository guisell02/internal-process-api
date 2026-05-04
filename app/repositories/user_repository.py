from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Repository layer responsible for user database operations.

    This layer should ONLY interact with the database and must NOT
    contain business logic or transaction management.
    """

    def __init__(self, db: Session):
        """
        Initialize repository with a SQLAlchemy session.

        Args:
            db (Session): Active SQLAlchemy database session.
        """
        self.db = db

    def create_user(self, user: User) -> User:
        """
        Persist a new user in the database.

        NOTE:
        - Does NOT commit the transaction.
        - Uses flush() to synchronize pending changes with the DB.
        - Uses refresh() to reload generated DB fields.

        Args:
            user (User): User entity to persist.

        Returns:
            User: Persisted user instance.
        """
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)

        return user

    def get_user_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by its ID.

        Args:
            user_id (int): User identifier.

        Returns:
            User | None: Found user or None if not found.
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email address.

        Args:
            email (str): User email.

        Returns:
            User | None: Found user or None if not found.
        """
        return self.db.query(User).filter(User.email == email).first()

    def update_user(self, user: User, **kwargs) -> User:
        """
        Update user attributes dynamically.

        NOTE:
        - Does NOT commit the transaction.

        Args:
            user (User): Existing user entity.
            **kwargs: Dynamic fields to update.

        Returns:
            User: Updated user entity.
        """
        for key, value in kwargs.items():
            setattr(user, key, value)

        self.db.flush()
        self.db.refresh(user)

        return user

    def delete_user(self, user: User) -> None:
        """
        Delete a user from the database.

        NOTE:
        - Does NOT commit the transaction.

        Args:
            user (User): User entity to delete.
        """
        self.db.delete(user)
        self.db.flush()
