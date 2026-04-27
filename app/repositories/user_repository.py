from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    """
    Repository layer for User entity.

    Handles ONLY database operations related to users.
    No business logic should be implemented here.
    """

    def __init__(self, db: Session):
        """
        Initialize repository with a database session.

        Args:
            db (Session): SQLAlchemy session instance.
        """
        self.db = db

    def create_user(self, user: User) -> User:
        """
        Persist a new user in the database.

        NOTE:
        - Does NOT commit the transaction.
        - Flush is used to send data to DB and detect errors early.

        Args:
            user (User): User instance to persist.

        Returns:
            User: Persisted user with DB-generated fields (e.g., ID).
        """
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by ID.

        Args:
            user_id (int): User identifier.

        Returns:
            User | None: Found user or None if not exists.
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.

        Args:
            email (str): User email.

        Returns:
            User | None: Found user or None if not exists.
        """
        return self.db.query(User).filter(User.email == email).first()

    def update_user(self, user: User, **kwargs) -> User:
        """
        Update user fields dynamically.

        Args:
            user (User): Existing user instance.
            **kwargs: Fields to update.

        Returns:
            User: Updated user instance.
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
            user (User): User instance to delete.
        """
        self.db.delete(user)
        self.db.flush()
