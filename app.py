"""Application entry point"""

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api.config import get_config
from api.model import db
from api.routes import init_routes
from api.service.handlers import error_handler
from api.util.utils import CustomJSONEncoder


def create_app(environment: str = "dev") -> Flask:
    """Initialize and setup flask app

    Returns:
        Flask: Flask application
    """
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    with app.app_context():
        app.config.update(get_config(environment))
        CORS(app)
        JWTManager(app)
        init_routes(app)
        db.init_app(app)
        db.create_all()
        error_handler.register_error_handlers(app)

    return app


if __name__ == "__main__":
    self_tracker_app = create_app()
    self_tracker_app.run()
