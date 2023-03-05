"""Common functions ragarding routes"""

from datetime import datetime

from flask import Blueprint
from flask_restful import Api

from api.constants import URL_PREFIX


def create_blueprint(name: str, import_name: str) -> Blueprint:
    """Create a blueprint for a route"""
    return Blueprint(name, import_name, url_prefix=URL_PREFIX)


def create_restful_api(bluprint: Blueprint) -> Api:
    """Create a RESTful API for a blueprint"""
    return Api(bluprint)


def convert_date_string_to_datetime(date_string: str) -> datetime:
    """Convert a date string to a datetime

    Args:
        date_string (str): Date string

    Returns:
        datetime: Converted datetime object
    """
    return datetime.strptime(date_string, "%Y-%m-%d")
