from app             import db

class Team(db.Model):
    __tablename__ = "teams"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column(db.String(100))
    brand             = db.Column(db.String(300))
    uniform_one       = db.Column(db.String(300))
    uniform_two       = db.Column(db.String(300))
    foundation_date   = db.Column(db.DateTime)
    activate          = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, name, brand, t_shirt, foundation_date, uniform_one, uniform_two):
        self.name            = name           
        self.brand           = brand          
        self.uniform_one     = uniform_one        
        self.uniform_two     = uniform_two        
        self.foundation_date = foundation_date
        self.activate        = activate  

    def __repr__(self):
        return "<Team %r>" % self.name