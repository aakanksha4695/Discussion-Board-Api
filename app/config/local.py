
class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/experdel"
    FLASK_DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = "development"
