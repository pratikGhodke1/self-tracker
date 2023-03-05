"""Common Utilities."""

import json
from datetime import date, datetime
from enum import Enum


# Update JSON Encoder
class CustomJSONEncoder(json.JSONEncoder):
    """Override Flask default JSONEncoder"""

    # pylint: disable=arguments-renamed
    def default(self, obj):
        """Override default method"""
        try:
            # Update date formatting
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()

            # Get Enum value
            if isinstance(obj, (Enum,)):
                return obj.value

            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return super().default(obj)
