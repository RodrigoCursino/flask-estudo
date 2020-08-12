from app.models.teams_players  import TeamsPlayers
from app.serialization         import model_teams_players
from flask_restplus            import Resource
from app.routes                import teams_players_route
from sqlalchemy.orm            import joinedload

@teams_players_route.route('/')
@teams_players_route.route('/<int:id>')
@teams_players_route.response(404, 'Teams Players not found')
@teams_players_route.response(500, 'Teams Players error')
@teams_players_route.param('id', 'The task identifier')
class TeamsPlayersController(Resource):
    @teams_players_route.marshal_with(model_teams_players)
    def get(self, id=None):
        if id == None:
            return list(TeamsPlayers.query.all()), 200
        
        return TeamsPlayers.query.filter_by(id=id).first(), 200
    
    def post(self):
        return {'Hello World': 'Hello World'}

teams_players_route.add_resource(TeamsPlayersController, '/', methods=['POST'])
teams_players_route.add_resource(TeamsPlayersController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



