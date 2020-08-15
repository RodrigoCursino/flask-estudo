from   app              import app
from   app.models.user  import User
import jwt
import datetime


class Auth():
    
    @staticmethod
    def encode_auth_token(user):
        """
            Gerando auth token
            :retun: string
        """
        try:
            payload = {
                'exp'     : datetime.datetime.utcnow() + datetime.timedelta(days=1,seconds=30),
                'iat'     : datetime.datetime.utcnow(),
                'id'      : user.id,
                'email'   : user.email,
                'username': user.username
            }

            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
            
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes um auth token
        :param request:
        :return: string|boolean
        """
        try:
            # auth_token  = ""
            # auth_header = request.headers.get('Authorization')
            
            # if auth_header:
            #     auth_token = auth_header.split(" ")[1]

            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            
            return Auth.__verify_user(payload)
        
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


    def __verify_user(payload):
        """
        Implementação da logica de verificação aqui
        :param jwt.decode:
        :return: boolean
        """
        user = User.query.filter_by(id=payload['id'],email=payload['email']).first()

        if user:
            return True
        else:
            return False