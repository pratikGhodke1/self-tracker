""" User model """

from werkzeug.security import check_password_hash, generate_password_hash

from api.model import db


class User(db.Model):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), default="")
    password_hash = db.Column(db.String(128))
    birth_date = db.Column(db.String)
    email = db.Column(db.String(50), unique=True)
    mobile = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    @property
    def password(self) -> None:
        """Set password field not accessible"""
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        """Hash password before saving."""
        if password:
            self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify user password

        Args:
            password (str): User password

        Returns:
            bool: Password verified?
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        """Return a string representation of User"""
        return f"<User: Name={self.first_name + self.last_name}, Email={self.email}>"

    def to_json(self) -> dict:
        """Convert User to JSON representation"""
        return {
            "id": self.id,
            "name": f"{self.first_name} {self.last_name}",
            "email": self.email,
            "mobile": self.mobile,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
