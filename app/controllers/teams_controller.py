from app.models.teams   import Team
from app.serialization  import model_team
from flask_restplus     import Resource
from app.routes         import teams_route
from sqlalchemy.orm     import joinedload

@teams_route.route('/')
@teams_route.route('/<int:id>')
@teams_route.response(404, 'Team not found')
@teams_route.response(500, 'Team error')
@teams_route.param('id', 'The task identifier')
class TeamController(Resource):
    @teams_route.marshal_with(model_team)
    def get(self, id=None):
        if id == None:
            return list(Team.query.all()), 200
        
        return Team.query.filter_by(id=id).first(), 200
    
    def post(self):
        return {'Hello World': 'Hello World'}

teams_route.add_resource(TeamController, '/', methods=['POST'])
teams_route.add_resource(TeamController, '/<id>', methods=['GET', 'PUT', 'DELETE'])



