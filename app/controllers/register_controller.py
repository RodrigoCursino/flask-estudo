
from app.services.login_service    import LoginService
from flask_restplus                import Resource
from app.routes                    import register_route
from app.serialization             import model_user
from sqlalchemy.orm                import joinedload
from flask                         import request

@register_route.route('/')
@register_route.response(404, 'Login not found')
@register_route.response(500, ';(')
class RegisterController(Resource):
    @register_route.expect(model_user)
    def post(self):
        return LoginService.register(register_route.payload)
       
register_route.add_resource(RegisterController, '/', methods=['POST'])



