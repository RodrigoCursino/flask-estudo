from app               import db
from app.models.posts  import Posts

class User(db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    name     = db.Column(db.String(100))
    password = db.Column(db.String(20))
    email    = db.Column(db.String(120), unique=True)
    activate = db.Column(db.Boolean, unique=False, default=True)
    posts    = db.relationship("Posts", back_populates="user", order_by=Posts.text)

    def __repr__(self):
        return "<User %r>" % self.id
