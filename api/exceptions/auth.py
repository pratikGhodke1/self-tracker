"""Auth Exceptions"""


class BadAuthHeader(Exception):
    """Bad Authentication Header with Invalid credentials"""

    def __init__(self) -> None:
        self.status_code = 400
        self.message = "Insufficient or missing credentials"
        super().__init__(self.message)

class UnauthorizedError(Exception):
    """User Unauthorized"""

    def __init__(self) -> None:
        self.status_code = 401
        self.message = "Invalid credentials"
        super().__init__(self.message)
