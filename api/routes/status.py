"""Application Status Endpoints"""

from flask_restful import Resource

from api.routes.routes_utils import create_blueprint, create_restful_api


class ApplicationHealth(Resource):
    """Application Health Endpoints"""

    def get(self) -> tuple[str, int]:
        """Check application health"""
        return "OK", 200


application_status_blueprint = create_blueprint("application_status", __name__)
application_status_api = create_restful_api(application_status_blueprint)

# Register routes
application_status_api.add_resource(ApplicationHealth, "/health")
