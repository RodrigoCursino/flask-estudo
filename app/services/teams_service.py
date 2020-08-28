from app.models.teams import Team 
from app              import db
from app              import bcrypt
from sqlalchemy       import exc

class TeamService():
    @staticmethod
    def create(payload):
        try:
            team = Team(payload['name'], payload['country'], payload['brand'], payload['color'], payload['alternateColor'], payload['abbreviation'], payload['foundation_date'], payload['uniform_one'], payload['uniform_two'])
            db.session.add(team)
            db.session.commit()
            return { 
                     "team"   : team.id,
                     "message": "sucesso ao inserir um time"
                   }, 201
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return {"message": "Todos eram até o nosso servidor :("}, 500

