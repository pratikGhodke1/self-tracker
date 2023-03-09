"""
Register routes to the flask app
"""
from flask import Flask

from api.routes.auth import auth_blueprint
from api.routes.status import application_status_blueprint
from api.routes.user import user_blueprint


def init_routes(app: Flask) -> None:
    """Initialize and assign the routes to flask app

    Args:
        app (Flask): Flask application
    """

    app.register_blueprint(application_status_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
