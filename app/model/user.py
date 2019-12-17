from flask_login import UserMixin

from .base_model import *
from .serialiser import BaseSchema


class User(UserMixin, Base):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def get_id(self):
        return self.user_id

class Comment(Base):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    comment = db.Column(db.String(1000))

# Schema
class UserSchema(BaseSchema):
    class Meta:
        model = User

class CommentSchema(BaseSchema):
    class Meta:
        model = Comment