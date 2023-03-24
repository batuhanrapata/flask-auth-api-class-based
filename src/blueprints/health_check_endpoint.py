import datetime
from datetime import timezone
from flask_restful import Resource

class HealthCheck(Resource):
    response= {'status': 200, "message": "OK", "timestamp": datetime.datetime.now(timezone.utc)}
    def get(self):
        return self.response, 200
    