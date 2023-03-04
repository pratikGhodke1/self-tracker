"""Application entry point"""

from flask import Flask

from api.utils.utils import CustomJSONEncoder
from api.config import get_config


def create_app(environment: str = "dev") -> Flask:
    """Initialize and setup flask app

    Returns:
        Flask: Flask application
    """
    app = Flask(__name__)
    app.json_provider_class = CustomJSONEncoder
    app.config.update(get_config(environment))
    return app


if __name__ == "__main__":
    scraper_app = create_app()
    scraper_app.run()
