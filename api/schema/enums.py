"""Enums for application"""

from enum import Enum


class RequestState(Enum):
    """Possible request states"""

    FAILED: str = "FAILED"
    SUCCESS: str = "SUCCESS"
    FORBIDDEN: str = "FORBIDDEN"
    BAD_REQUEST: str = "BAD_REQUEST"
    UNAUTHORIZED: str = "UNAUTHORIZED"
