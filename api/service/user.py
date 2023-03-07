"""User Service"""

from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from api.exceptions import generate_response
from api.exceptions.user import UserAlreadyExists, UserNotExists
from api.model import db
from api.model.user import User
from api.schema.enums import RequestState


def get_all_users(args: dict) -> list[dict]:
    """Fetch all users from the database

    Args:
        args (dict): Query parameters

    Returns:
        list[dict]: List of all users (paginated)
    """
    page = args.get("page", 1)
    items_per_page = args.get("items_per_page", 10)
    users = User.query.paginate(
        page=int(page), per_page=int(items_per_page), error_out=False
    ).items
    return [user.to_json() for user in users]


def add_user(new_user_info: dict) -> dict:
    """Add a new user to the database

    Args:
        new_user_info (dict): New user information

    Raises:
        UserAlreadyExists: User already exists error

    Returns:
        dict: Added user information
    """
    email = new_user_info["email"]
    mobile = new_user_info["mobile"]

    existing_user = User.query.filter(
        or_(User.email == email, User.mobile == mobile)
    ).first()

    if existing_user:
        raise UserAlreadyExists()

    new_user = User(**new_user_info)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_json()


# Single User Operations
def get_user(user_id: int) -> dict:
    """Get a user by ID

    Args:
        user_id (int): User ID

    Raises:
        UserNotExists: User does not exists error

    Returns:
        dict: Fetched user information
    """
    user = User.query.get(user_id)

    if not user:
        raise UserNotExists(user_id)

    return user.to_json()


def update_user(user_id: int, update_user_info: dict) -> dict:
    """Update a user by ID

    Args:
        user_id (int): User ID
        update_user_info (dict): User information to update

    Raises:
        UserNotExists: User does not exists error

    Returns:
        dict: Updated user information
    """
    try:
        user = User.query.filter_by(id=user_id).first()

        if not user:
            raise UserNotExists(user_id)

        for field, value in update_user_info.items():
            setattr(user, field, value)

        user.updated_at = db.func.now()
        db.session.commit()
        return generate_response(RequestState.SUCCESS, f"Updated User {[user_id]}")

    except IntegrityError as error:
        db.session.rollback()
        raise UserAlreadyExists() from error


def delete_user(user_id: int) -> None:
    """Delete a user by ID

    Args:
        user_id (int): User ID

    Raises:
        UserNotExists: User does not exists error
    """
    user = User.query.get(user_id)

    if not user:
        raise UserNotExists(user_id)

    db.session.delete(user)
    db.session.commit()
