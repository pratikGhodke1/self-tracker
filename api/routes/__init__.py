"""
Register routes to the flask app
"""
from flask import Flask
from api.routes.status import application_status_blueprint


def init_routes(app: Flask) -> None:
    """Initialize and assign the routes to flask app

    Args:
        app (Flask): Flask application
    """

    app.register_blueprint(application_status_blueprint)
