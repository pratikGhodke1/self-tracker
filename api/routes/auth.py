"""Authentication Routes"""

from flask import request, make_response
from flask_restful import Resource

from api.exceptions import generate_response
from api.exceptions.auth import BadAuthHeader, UnauthorizedError
from api.routes.routes_utils import create_blueprint, create_restful_api
from api.model.user import User
from api.service.handlers.authentication import get_jwt_token


class Login(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            raise BadAuthHeader()

        user: User = User.query.filter_by(email=auth.username).first()

        if user and user.verify_password(auth.password):
            return make_response(
                generate_response(
                    custom_fields={"access_token": get_jwt_token(user.id)}
                ),
                200,
            )

        raise UnauthorizedError()


auth_blueprint = create_blueprint("auth", __name__)
auth_api = create_restful_api(auth_blueprint)

# Register routes
auth_api.add_resource(Login, "/login")
