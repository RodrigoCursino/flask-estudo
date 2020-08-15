from app             import db 

class Posts(db.Model):
    __tablename__ = "posts"
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text     = db.Column(db.String(100), unique=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('users.id'))

    user =  db.relationship('User', foreign_keys=user_id)

    def __init__(self, text, user_id):
        self.text    = text
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.text