"""Error Handler Service"""

from flask import Flask, request

from api.exceptions import auth, user
from api.constants import ERROR_HANDLER
from api.schema.enums import RequestState
from api.util.logger import init_logger

logger = init_logger(__name__, ERROR_HANDLER, request)


def _error_response(error: Exception) -> tuple[dict, int]:
    """Error response generator callback

    Args:
        error (Exception): Raised error exception

    Returns:
        tuple[dict, int]: Flask error response and status code
    """
    try:
        status_code = error.status_code
    except AttributeError:
        status_code = 500

    error_message = ("[INTERNAL ERROR] " if status_code == 500 else "") + str(error)
    logger.error(error_message)

    return (
        {
            "status": RequestState.FAILED,
            "message": error_message,
        },
        status_code,
    )


def register_error_handlers(app: Flask):
    """register error handlers to flask application"""
    app.register_error_handler(user.UserAlreadyExists, _error_response)
    app.register_error_handler(user.UserNotExists, _error_response)
    app.register_error_handler(auth.BadAuthHeader, _error_response)
    app.register_error_handler(auth.UnauthorizedError, _error_response)
