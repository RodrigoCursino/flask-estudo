from app.models.user               import User
from app.services.login_service    import LoginService
from app.utils.oauth               import Auth
from app.serialization             import model_user
from flask_restplus                import Resource
from app.routes                    import users_route
from sqlalchemy.orm                import joinedload
from flask                         import request

@users_route.route('/')
@users_route.route('/<int:id>')
@users_route.response(404, 'User not found')
@users_route.response(500, 'Desculpe Erro No servidor')
@users_route.param('id', 'The task identifier')
class UserController(Resource):
    @users_route.marshal_with(model_user, code=200)
    def get(self, id=None):
        if id == None:
            return list(User.query.options(joinedload('posts')))
        
        return User.query.options(joinedload('posts')).filter_by(id=id).first()
    
    @users_route.expect(model_user)
    def post(self):
        return LoginService.register(users_route.payload)
       
users_route.add_resource(UserController, '/', methods=['POST'])
users_route.add_resource(UserController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



