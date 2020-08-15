from app.models.user import User
from app.utils.oauth import Auth
from app             import db
from app             import bcrypt
from sqlalchemy      import exc

class LoginService():
    
    @staticmethod
    def login(payload):
        user = User.query.filter_by(email=payload['email']).first()
        token = ""
        if(user and bcrypt.check_password_hash(user.password, payload['password'])):

            token = Auth.encode_auth_token(user)
            
            return {
                'token' : str(token, 'utf-8'),
                'user'  : user.username,
                'email' : user.email,
            }, 200
           
        return {
            'message': 'Senha ou email não estão corretos'
        }, 401

    
    @staticmethod
    def register(payload):
        try:
            if(not User.query.filter_by(email=payload['email']).first()):
                user = User(payload['username'], payload['name'], payload['password'], payload['email'])
                db.session.add(user)
                db.session.commit()

                return {"message": "sucesso ao inserir usuário"}, 201
            
            return {"message": "Usuário já cadastrado"}, 422 
            
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return {"message": "Todos eram até o nosso servidor :("}, 500


