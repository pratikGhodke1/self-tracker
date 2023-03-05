"""Exception response generator"""

from typing import Optional

from api.schema.enums import RequestState

# --------------------------- Custom Error Classes --------------------------- #


class UserAlreadyExists(Exception):
    """User already exists exception"""

    def __init__(self) -> None:
        self.status_code = 400
        self.message = "User with same email OR mobile already exists"
        super().__init__(self.message)


class UserNotExists(Exception):
    """User does not exists exception"""

    def __init__(self, user_id: int) -> None:
        self.status_code = 404
        self.message = f"User [{user_id}] does not exists"
        super().__init__(self.message)


# ---------------------------------------------------------------------------- #


def generate_response(
    status: RequestState, message: str, custom_fields: Optional[dict] = None
) -> dict:
    """Generate error response body

    default fields:
    {
        "status": "FAILED" | "SUCCESS",
        "message": message
    }

    Args:
        status (RequestState): Request Status
        message (str): Response message
        custom_fields (dict): Custom response fields

    Returns:
        dict: Error response body
    """
    custom_fields = custom_fields or {}
    return dict({"status": status, "message": message}, **custom_fields)


# ---------------------------------------------------------------------------- #


def _error_response(error: Exception) -> tuple[dict, int]:
    """Error response generator

    Args:
        error (Exception): Raised error exception

    Returns:
        tuple[dict, int]: Flask error response and status code
    """
    try:
        status_code = error.status_code
    except AttributeError:
        status_code = 500

    return {
        "status": RequestState.FAILED,
        "message": ("[INTERNAL ERROR] " if status_code == 500 else "") + str(error),
    }, status_code


def register_errorhandlers(app):
    """register error handlers to flask application"""
    app.register_error_handler(UserAlreadyExists, _error_response)
    app.register_error_handler(UserNotExists, _error_response)
