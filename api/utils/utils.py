"""Common Utilities."""

import json
from datetime import date, datetime


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
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return super().default(obj)
