"""Exception response generator"""

from typing import Optional
from api.schema.enums import RequestState

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
