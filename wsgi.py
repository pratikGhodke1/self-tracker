"""WSGI application"""

from app import create_app

application = create_app(environment="prod")
