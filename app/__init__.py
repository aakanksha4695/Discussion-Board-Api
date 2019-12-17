from flask import Flask
from flask_restful import Api
from flask import Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from app.config import  Config
from .model import * 


# print(db)
# create instance of flask class 
flask_app = Flask(__name__)
flask_app.secret_key = 'secretkey'

# flask login
login_manager = LoginManager()
login_manager.init_app(flask_app)

flask_app.config.from_object(Config)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

flask_app.register_blueprint(api_bp, url_prefix='/api')

# initialise sqlalchemy
db.init_app(flask_app)

# initialise marshmallow
ma.init_app(flask_app)

# initialise blueprints
api.init_app(api_bp)

# initialise flask migrations
migrate.init_app(flask_app, db)

from app import urls

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
