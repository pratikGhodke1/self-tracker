"""Authentication Handler"""

from functools import wraps

from flask_jwt_extended import create_access_token, verify_jwt_in_request


def get_jwt_token(user_id: int) -> str:
    """Get JWT Token"""
    return create_access_token(user_id)


def login_required():
    """Login required decorator"""

    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            return func(*args, **kwargs)

        return decorator

    return wrapper
