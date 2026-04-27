"""
Manual test script for database session behavior.

This script is used to:
- test database connection
- understand transactions (commit / rollback)
- validate constraints (unique email)

Not part of production code.
"""

from app.database.session import SessionLocal
from app.models.user import User
from datetime import datetime, UTC
import logging

# configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SessionLocal()

new_user = User(
    first_name="Guisella",
    last_name="Urbina",
    email="guisell2@example.com",
    password_hash="123",
    role_id=1,
    is_active=True,
    created_at=datetime.now(UTC),
    updated_at=datetime.now(UTC),
)

try:
    db.add(new_user)
    logger.info(f"Creating user with email: {new_user.email}")

    db.commit()
    logger.info("User successfully created")

except Exception as e:
    db.rollback()
    logger.error(f"Database error occurred: {e}")

finally:
    db.close()
    logger.info("Database session closed")
