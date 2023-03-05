"""Application entry point"""

from flask import Flask
from flask_cors import CORS

from api.config import get_config
from api.model import db
from api.routes import init_routes
from api.util.utils import CustomJSONEncoder

def create_app(environment: str = "dev") -> Flask:
    """Initialize and setup flask app

    Returns:
        Flask: Flask application
    """
    app = Flask(__name__)
    with app.app_context():
        app.json_provider_class = CustomJSONEncoder
        app.config.update(get_config(environment))
        CORS(app)
        init_routes(app)
        db.init_app(app)
        db.create_all()

    return app


if __name__ == "__main__":
    scraper_app = create_app()
    scraper_app.run()
