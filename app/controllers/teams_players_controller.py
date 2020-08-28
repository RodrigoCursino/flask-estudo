from app.services.teams_players_service  import TeamsPlayersService
from app.serialization                   import model_teams_players
from flask_restplus                      import Resource
from flask                               import request
from app.utils.oauth                     import Auth
from app.routes                          import teams_players_route
from sqlalchemy.orm                      import joinedload
import json

@teams_players_route.route('/')
@teams_players_route.route('/<pais>/<int:id>')
@teams_players_route.route('/<pais>')
@teams_players_route.response(404, 'Teams Players not found')
@teams_players_route.response(500, 'Teams Players error')
@teams_players_route.param('id', 'The Team identifier')
class TeamsPlayersController(Resource):
    def get(self, id=None, pais=None):
        if(Auth.decode_auth_token(request)):
            return TeamsPlayersService.list(pais,id)
        else:
            return {"Mensagem":"Não Permitido"}, 401
    def post(self):
        return {'Hello World': 'Hello World'}

teams_players_route.add_resource(TeamsPlayersController, '/', methods=['POST'])
teams_players_route.add_resource(TeamsPlayersController, '/<pais>', methods=['GET'])
teams_players_route.add_resource(TeamsPlayersController, '/<pais>/<id>', methods=['GET', 'PUT', 'DELETE'])



