"""
Domain exceptions related to user operations.
"""


class UserAlreadyExistsError(Exception):
    """
    Raised when attempting to create or update
    a user with an email that already exists.
    """

    pass


class UserNotFoundError(Exception):
    """
    Raised when a requested user does not exist.
    """

    pass
