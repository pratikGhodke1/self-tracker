"""
Logger module for logging
"""

# Imports
import logging

from api.config import SETTINGS


# pylint: disable=R0903
class AppFilter(logging.Filter):
    """Logger filter - add "app_name" field in log string"""

    def __init__(self, app_name: str, request):
        self.app_name = app_name
        self.request = request
        super().__init__()

    def filter(self, record):
        record.app_name = self.app_name
        if self.request != "":
            record.endpoint = f"{self.request.path} |"
            record.method = self.request.method
        else:
            record.endpoint = ""
            record.method = ""

        return True


# Initialize Logger
def init_logger(logger_name, app_name, request="") -> logging.Logger:
    """Initialize the Logger

    Args:
        logger_name (str): Logger Name
        app_name (str): Service Name
        request (str, optional): Request object to access routes & method. Defaults to "".

    Returns:
        logging.Logger: Logger object
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addFilter(AppFilter(app_name=app_name, request=request))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | [%(app_name)s] | %(method)s %(endpoint)s %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(SETTINGS.LOG_FILE_PATH)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
