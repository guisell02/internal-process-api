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

db = SessionLocal()

# create user
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
    print(new_user.email)
    db.commit()

except Exception as e:
    db.rollback()
    print(f"el error es: {e}")

finally:
    db.close()
