"""
Password hashing and verification utilities.

This module centralizes password security operations
used across the application.

Responsibilities:
- Hash plain-text passwords before persistence
- Verify passwords during authentication
- Encapsulate hashing algorithm configuration

Using a centralized security module ensures that
hashing behavior remains consistent and easy to
update across the system.
"""

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Generate a secure hash for a plain-text password.

    Args:
        password: Raw password provided by the user.

    Returns:
        Secure hashed password string.
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify whether a plain-text password matches
    its stored hash.

    Args:
        plain_password: Raw password provided by the user.
        hashed_password: Previously stored password hash.

    Returns:
        True if the password is valid, otherwise False.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )
