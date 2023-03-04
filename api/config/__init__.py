"""
Application configuration
"""

import os
from pydantic import BaseSettings


class GlobalSettings(BaseSettings):
    """Global Settings"""

    FLASK_APP: str = "app.py"
    URL_PREFIX: str = "/api/v1"


class DevConfig(GlobalSettings):
    """Development configuration"""

    ENV: str = "development"
    DEBUG: bool = True
    SERVER_NAME: str = "localhost:5000"


class TestingConfig(DevConfig):
    """Testing configuration"""

    ENV: str = "testing"
    TESTING: bool = True
    SERVER_NAME: str = "localhost:5001"


class ProdConfig(GlobalSettings):
    """Production configuration"""

    ENV: str = "production"
    DEBUG: bool = False
    SERVER_NAME: str = "localhost:5002"


def get_config(env_name: str) -> dict:
    """Get configuration by environment name

    Args:
        env_name (str): Environment name

    Returns:
        dict: Configuration dictionary
    """

    return {
        "dev": DevConfig().dict(),
        "test": TestingConfig().dict(),
        "prod": ProdConfig().dict(),
    }.get(env_name)
