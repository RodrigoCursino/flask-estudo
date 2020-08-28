from app.models.players       import Player
from app.models.teams_players import TeamsPlayers
from app                      import db
from app                      import bcrypt
from sqlalchemy               import exc

class PlayerService():
    @staticmethod
    def create(payload):
        try:
            player = Player( payload['name'], payload['country'], payload['position'], payload['height'], payload['weight'], payload['picture'], payload['feature'], payload['default_leg'], payload['birth_date'])
            db.session.add(player)
            db.session.commit()

            team_player = TeamsPlayers( payload['date_begin'], payload['date_end'], payload['player_number'], payload['team_id'], player.id)
            db.session.add(team_player) 
            db.session.commit()
            return {"message": "sucesso ao inserir um jogador"}, 201
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return {"message": "Todos eram até o nosso servidor :("}, 500

