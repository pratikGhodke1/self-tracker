"""Application entry point"""

from flask import Flask

from api.config import get_config
from api.routes import init_routes
from api.util.utils import CustomJSONEncoder


def create_app(environment: str = "dev") -> Flask:
    """Initialize and setup flask app

    Returns:
        Flask: Flask application
    """
    app = Flask(__name__)
    app.json_provider_class = CustomJSONEncoder
    init_routes(app)
    app.config.update(get_config(environment))

    return app


if __name__ == "__main__":
    scraper_app = create_app()
    scraper_app.run()
