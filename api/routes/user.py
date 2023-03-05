"""User routes"""

from flask import request, make_response
from flask_restful import Resource
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from api.exceptions import generate_response, UserAlreadyExists, UserNotExists
from api.model import db
from api.model.user import User
from api.routes.routes_utils import create_blueprint, create_restful_api
from api.schema.enums import RequestState


class UsersAPI(Resource):
    """API to add and list users"""

    def post(self):
        """Create a new user"""
        email = request.json.get("email", "")
        mobile = request.json.get("mobile", "")

        user = User.query.filter(
            or_(User.email == email, User.mobile == mobile)
        ).first()

        if user:
            raise UserAlreadyExists()

        user = User(**request.json)
        db.session.add(user)
        db.session.commit()
        return make_response(user.to_json(), 201)

    def get(self):
        """Get list of all users"""
        page = request.args.get("page", 1)
        items_per_page = request.args.get("items_per_page", 10)
        users = User.query.paginate(
            page=int(page), per_page=int(items_per_page), error_out=False
        ).items
        return make_response([user.to_json() for user in users], 201)


class UserAPI(Resource):
    """API to handle user related operations"""

    def get(self, user_id: int):
        """Get user by id"""
        user = User.query.get(user_id)

        if not user:
            raise UserNotExists(user_id)

        return make_response(user.to_json(), 200)

    def put(self, user_id: int):
        """Get user by id"""
        try:
            user = User.query.filter_by(id=user_id).first()

            if not user:
                raise UserNotExists(user_id)

            for field, value in request.json.items():
                setattr(user, field, value)

            user.updated_at = db.func.now()
            db.session.commit()
            return make_response(
                generate_response(RequestState.SUCCESS, f"Updated User {[user_id]}"),
                200,
            )

        except IntegrityError:
            db.session.rollback()
            raise UserAlreadyExists()

    def delete(self, user_id: int):
        """Delete a user by id."""
        user = User.query.get(user_id)

        if not user:
            raise UserNotExists(user_id)

        db.session.delete(user)
        db.session.commit()
        return "", 204


user_blueprint = create_blueprint("user", __name__)
user_api = create_restful_api(user_blueprint)

# Register routes
user_api.add_resource(UsersAPI, "/user")
user_api.add_resource(UserAPI, "/user/<int:user_id>")
