from app             import db

class Team(db.Model):
    __tablename__ = "teams"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column(db.String(200))
    country           = db.Column(db.String(100))
    brand             = db.Column(db.String(800))
    color             = db.Column(db.String(20))
    alternateColor    = db.Column(db.String(20))
    abbreviation      = db.Column(db.String(5))
    foundation_date   = db.Column(db.DateTime, nullable=True)
    uniform_one       = db.Column(db.String(300), nullable=True)
    uniform_two       = db.Column(db.String(300), nullable=True)
    activate          = db.Column(db.Boolean, unique=False, default=True)
    players           = db.relationship('Player', secondary = 'teams_players')

    def __init__(self, name, country, brand, color, alternateColor, abbreviation, foundation_date, uniform_one, uniform_two):
        self.name            = name           
        self.country         = country           
        self.brand           = brand          
        self.color           = color          
        self.alternateColor  = alternateColor          
        self.abbreviation    = abbreviation          
        self.uniform_one     = uniform_one        
        self.uniform_two     = uniform_two        
        self.foundation_date = foundation_date

    def __repr__(self):
        return "<Team %r>" % self.name