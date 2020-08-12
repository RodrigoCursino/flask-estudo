from   app                        import db

class Player(db.Model):
    __tablename__     = "players"
    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100))
    picture           = db.Column(db.String(300))
    feature           = db.Column(db.TEXT(1000))
    default_leg       = db.Column(db.String(34))
    birth_date        = db.Column(db.DateTime)
    activate          = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, name, picture, feature, default_leg, birth_date):
        SELF.name        = name       
        SELF.picture     = picture    
        SELF.feature     = feature    
        SELF.default_leg = default_leg
        SELF.birth_date  = birth_date  

    def __repr__(self):
        return "<Player %r>" % self.name