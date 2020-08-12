from app.models.posts    import Posts
from app.serialization   import model_posts
from flask_restplus      import Resource
from app.routes          import posts_route
from sqlalchemy.orm      import joinedload

@posts_route.route('/')
@posts_route.route('/<int:id>')
@posts_route.response(404, 'Post not found')
@posts_route.param('id', 'The post identifier')
class PostController(Resource):
    @posts_route.marshal_with(model_posts)
    def get(self, id=None):
        if id == None:
            return list(Posts.query.all()), 200
        
        return Posts.query.filter_by(id=id).first(), 200
    
    def post(self):
        return {'Hello World': 'Hello World'}

posts_route.add_resource(PostController, '/', methods=['POST'])
posts_route.add_resource(PostController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



