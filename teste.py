from app.services.login_service import LoginService
from app             import bcrypt

password = '123456'
username = 'teste'
email = 'teste@teste.com'

# print("Login ",  bcrypt.generate_password_hash('123456'))
# print("Login ", LoginService.login(password, username, email))