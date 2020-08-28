from   app                        import db

class Player(db.Model):
    __tablename__     = "players"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column(db.String(100))
    country           = db.Column(db.String(100))
    position          = db.Column(db.String(1))
    height            = db.Column(db.Float(precision=2, asdecimal=False))
    weight            = db.Column(db.Integer())
    picture           = db.Column(db.String(300), nullable=True)
    feature           = db.Column(db.TEXT(1000), nullable=True)
    default_leg       = db.Column(db.String(34), nullable=True)
    birth_date        = db.Column(db.DateTime)
    activate          = db.Column(db.Boolean, unique=False, default=True)
    teams             = db.relationship('Team', secondary = 'teams_players')

    def __init__(self, name, country, position, height, weight, picture, feature, default_leg, birth_date):
        self.name        = name       
        self.country     = country       
        self.position    = position       
        self.height      = height       
        self.weight      = weight      
        self.picture     = picture    
        self.feature     = feature    
        self.default_leg = default_leg
        self.birth_date  = birth_date  

    def __repr__(self):
        return "<Player %r>" % self.name