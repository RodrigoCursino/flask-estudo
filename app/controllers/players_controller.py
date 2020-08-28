from app.models.players           import Player
from app.services.players_service import PlayerService
from app.serialization            import model_player
from flask_restplus               import Resource
from app.routes                   import players_route
from sqlalchemy.orm               import joinedload

@players_route.route('/')
@players_route.route('/<int:id>')
@players_route.response(404, 'User not found')
@players_route.response(500, 'User error')
@players_route.param('id', 'The task identifier')
class PlayerController(Resource):
    @players_route.marshal_with(model_player)
    def get(self, id=None):
        if id == None:
            return list(Player.query.all()), 200
        
        return Player.query.filter_by(id=id).first(), 200
    
    @players_route.expect(model_player)
    def post(self):
        return PlayerService.create(players_route.payload)

players_route.add_resource(PlayerController, '/', methods=['POST'])
players_route.add_resource(PlayerController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



