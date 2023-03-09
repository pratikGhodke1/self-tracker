"""User Exceptions"""


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
