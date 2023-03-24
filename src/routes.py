

from src.blueprints.health_check_endpoint import HealthCheck
from src.blueprints.list_users_endpoint import ListUsers
from src.blueprints.login_endpoint import Login
from src.blueprints.register_endpoint import Register
def routes(app): 
    app.add_resource(Login, '/api/v1/login')
    app.add_resource(Register, '/api/v1/register')
    app.add_resource(ListUsers, '/api/v1/list_users')
    app.add_resource(HealthCheck, '/api/v1/health_check')
    