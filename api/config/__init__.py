"""
Application configuration
"""
# pylint: disable=R0903

import os

from pydantic import BaseSettings

APPLICATION_ENV = os.environ.get("ENV", "development")


class GlobalSettings(BaseSettings):
    """Global Settings"""

    FLASK_APP: str = "app.py"
    URL_PREFIX: str = "/api/v1"
    LOG_FILE_PATH: str = "./api.log"
    JWT_SECRET_KEY: str = "very-secret-key"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevConfig(GlobalSettings):
    """Development configuration"""

    ENV: str = "development"
    DEBUG: bool = True
    SERVER_NAME: str = "localhost:5000"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///dev.sqlite3"


class TestingConfig(DevConfig):
    """Testing configuration"""

    ENV: str = "testing"
    TESTING: bool = True
    SERVER_NAME: str = "localhost:5001"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///test.sqlite3"


class ProdConfig(GlobalSettings):
    """Production configuration"""

    ENV: str = "production"
    DEBUG: bool = False
    SERVER_NAME: str = "localhost:5002"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///prod.sqlite3"


SETTINGS = {
    "development": DevConfig(),
    "testing": TestingConfig(),
    "production": ProdConfig(),
}.get(APPLICATION_ENV)
