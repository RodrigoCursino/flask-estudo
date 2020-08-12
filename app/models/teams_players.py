from app             import db

class TeamsPlayers(db.Model):
    __tablename__     = "teams_players"
    id                = db.Column(db.Integer, primary_key=True)
    date_begin        = db.Column(db.DateTime)
    date_end          = db.Column(db.DateTime, nullable=True)
    player_number     = db.Column(db.Integer)
    player_id         = db.Column(db.Integer, db.ForeignKey('players.id'), primary_key=True)
    team_id           = db.Column(db.Integer, db.ForeignKey('teams.id'), primary_key=True)
    team              = db.relationship('Team', foreign_keys=team_id)
    player            = db.relationship('Player', foreign_keys=player_id)
    activate          = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, date_begin, date_end, player_number, team_id, player_id):
        self.date_begin    = date_begin   
        self.date_end      = date_end     
        self.player_number = player_number   
        self.team_id       = team_id   
        self.player_id     = player_id   
         
    def __repr__(self):
        return "<TeamsPlayers %r>" % self.date_begin