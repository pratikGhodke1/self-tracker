"""Test API version"""

from api import __version__


def test_version() -> None:
    """Test API version"""
    assert __version__ == "0.1.0"
