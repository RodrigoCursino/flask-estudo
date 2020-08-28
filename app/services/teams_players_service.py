from app.models.teams_players import TeamsPlayers
from app.models.teams         import Team
from app.models.players       import Player    
from app                      import db
from app                      import bcrypt
from sqlalchemy               import exc

class TeamsPlayersService():
    @staticmethod
    def list(pais, id=None):
        if(id):
            data = TeamsPlayers.query.join(Player).join(Team).filter(Team.country == pais, Team.id == id,TeamsPlayers.activate == True).group_by(Player.id).group_by(Team.id).all()
        else:
            data = TeamsPlayers.query.join(Player).join(Team).filter(Team.country == pais,TeamsPlayers.activate == True).group_by(Player.id).group_by(Team.id).all()
        
        if (not data):
            return [], 404

        response = {}
        
        for d in data:
            response[d.team.id] = {
                    'id'                 : d.team.id,
                    'name'               : d.team.name,
                    'brand'              : d.team.brand,
                    'color'              : d.team.color,
                    'country'            : d.team.country,
                    'alternateColor'     : d.team.alternateColor,
                    'abbreviation'       : d.team.abbreviation,
                    'uniform_one'        : d.team.uniform_one,
                    'uniform_two'        : d.team.uniform_two,
                    'foundation_date'    : d.team.foundation_date,
                    "players"            : list(filter(lambda x : x.team_id == d.team_id, data))
                }

        response_aux = []                   
        for x in response: 
            aux = []
            for i in response[x]["players"]:
                aux.append({
                        "name"          : i.player.name,
                        'team_id'       : i.team_id,
                        'country'       : i.player.country, 
                        'position'      : i.player.position, 
                        'player_number' : i.player_number, 
                        'height'        : i.player.height, 
                        'weight'        : i.player.weight,          
                        'picture'       : i.player.picture,         
                        'feature'       : i.player.feature,         
                        'default_leg'   : i.player.default_leg,    
                        'birth_date'    : i.player.birth_date,       
                        'date_begin'    : i.date_begin,       
                        'date_end'      : i.date_end,  
                })
            response[x]["players"] = aux
            response_aux.append(response[x])
        return response_aux, 200 