from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions.user_exceptions import UserAlreadyExistsError


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers for the FastAPI application.

    This centralizes error handling, translating domain exceptions
    into standardized HTTP responses.
    """

    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        request: Request, exc: UserAlreadyExistsError
    ) -> JSONResponse:
        """
        Handle UserAlreadyExistsError and return a 409 Conflict response.
        """
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "error": "Conflict",
                "message": str(exc),
                "code": "USER_ALREADY_EXISTS",
            },
        )
