from app               import db, bcrypt, app
from app.models.posts  import Posts

class User(db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    name     = db.Column(db.String(100))
    password = db.Column(db.String(255))
    email    = db.Column(db.String(120), unique=True)
    activate = db.Column(db.Boolean, unique=False, default=True)
    posts    = db.relationship("Posts", back_populates="user", order_by=Posts.text)

    def __init__(self, username, name, password, email):
        self.username = username
        self.name     = name
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.email    = email


    def __repr__(self):
        return "<User %r>" % self.id
