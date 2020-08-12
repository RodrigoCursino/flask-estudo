from app.models.user    import User
from app.serialization  import model_user
from flask_restplus     import Resource
from app.routes         import users_route
from sqlalchemy.orm     import joinedload

@users_route.route('/')
@users_route.route('/<int:id>')
@users_route.response(404, 'User not found')
@users_route.response(500, 'User error')
@users_route.param('id', 'The task identifier')
class UserController(Resource):
    @users_route.marshal_with(model_user)
    def get(self, id=None):
        if id == None:
            return list(User.query.options(joinedload('posts'))), 200
        
        return User.query.options(joinedload('posts')).filter_by(id=id).first(), 200
    
    def post(self):
        return {'Hello World': 'Hello World'}

users_route.add_resource(UserController, '/', methods=['POST'])
users_route.add_resource(UserController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



