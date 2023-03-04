"""Common functions ragarding routes"""

from flask import Blueprint
from flask_restful import Api
from api.constants import URL_PREFIX


def create_blueprint(name: str, import_name: str) -> Blueprint:
    """Create a blueprint for a route"""
    return Blueprint(name, import_name, url_prefix=URL_PREFIX)


def create_restful_api(bluprint: Blueprint) -> Api:
    """Create a RESTful API for a blueprint"""
    return Api(bluprint)
