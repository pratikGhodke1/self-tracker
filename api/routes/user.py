"""User routes"""

from flask import make_response, request
from flask_pydantic import validate
from flask_restful import Resource

from api.constants import USER_SERVICE
from api.routes.routes_utils import create_blueprint, create_restful_api
from api.schema.validation import UserPostRequest, UserPutRequest
from api.service import user
from api.service.handlers import authentication
from api.util.logger import init_logger

logger = init_logger(__name__, USER_SERVICE, request)


class UsersAPI(Resource):
    """API to add and list users"""

    @validate()
    def post(self, body: UserPostRequest):
        """Create a new user"""
        logger.info("Received request to create a new user")
        added_user = user.add_user(body.dict())
        logger.info(f"User [id={added_user['id']}] added")
        return make_response(added_user, 201)

    @authentication.login_required()
    def get(self):
        """Get list of all users"""
        logger.info("Received request to list all users")
        users = user.get_all_users(request.args)
        logger.info(f"Returning {len(users)} users. [args={request.args.to_dict()}]")
        return make_response(users, 200)


class UserAPI(Resource):
    """API to handle user related operations"""

    @authentication.login_required()
    def get(self, user_id: int):
        """Get user by id"""
        logger.info(f"Received request to get user: {user_id}")
        fetched_user = user.get_user(user_id)
        logger.info(f"Returning user: {user_id}")
        return make_response(fetched_user, 200)

    @authentication.login_required()
    @validate()
    def put(self, user_id: int, body: UserPutRequest):
        """Get user by id"""
        logger.info(f"Received request to update user: {user_id}")
        updated_user_response = user.update_user(user_id, body.dict(exclude_unset=True))
        logger.info(f"Updated user: {user_id}")
        return make_response(updated_user_response, 200)

    @authentication.login_required()
    def delete(self, user_id: int):
        """Delete a user by id."""
        logger.info(f"Received request to delete user: {user_id}")
        user.delete_user(user_id)
        logger.info(f"Deleted user: {user_id}")
        return "", 204


user_blueprint = create_blueprint("user", __name__)
user_api = create_restful_api(user_blueprint)

# Register routes
user_api.add_resource(UsersAPI, "/user")
user_api.add_resource(UserAPI, "/user/<int:user_id>")
