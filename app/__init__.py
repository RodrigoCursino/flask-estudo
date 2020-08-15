from flask            import Flask
from flask_restplus   import Api
from flask_sqlalchemy import SQLAlchemy
from flask_script     import Manager
from flask_migrate    import Migrate, MigrateCommand
from flask_cors       import CORS
from flask_bcrypt     import Bcrypt

# app configure
app = Flask(__name__)
app.config.from_object('config')
api    = Api(app)
bcrypt = Bcrypt(app)
CORS(app, resources={r"/*": {"origins": "*"}})
# app configure

#db orm confugure
db      = SQLAlchemy(app)
migrate = Migrate(app, db)

""" db comands
$ db init
$ db stamp head
$ db migrate
$ db upgrade
"""
#db orm confugure

#configuração de db scripts
manager = Manager(app)
manager.add_command('db', MigrateCommand)
#configuração de db scripts

#app
from app         import controllers
from app.models  import tables
#app