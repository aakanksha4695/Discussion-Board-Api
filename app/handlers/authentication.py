from datetime import datetime, timedelta
from sqlalchemy.exc import DataError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .base_handler import *
from app.model.user import User, UserSchema, Comment, CommentSchema
from app import login_manager


class SignupHandler(BaseHandler):

    def post(self):
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        print(name)
        if not name:
            return self.return_json(status='400', msg="Please enter your Name")
        elif not email:
            return self.return_json(status='400', msg="Please enter your Email ID")
        elif not password:
            return self.return_json(status='400', msg="Please enter your Password")
        else:
            user = User.query.filter_by(
                email=email).first()  # if this returns a user, then the email already exists in database

            if user:  # if a user is found, we want to redirect back to signup page so user can try again
                return self.return_json(status=200, msg="User already exist.")

            # create new user with the form data. Hash the password so plaintext version isn't saved.
            new_user = UserSchema().load({'email': email,
                                          'name': name,
                                          'password': generate_password_hash(password, method='sha256')
                                          }).data

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            return self.return_json(status=200, msg="User account created.")


class LoginHandler(BaseHandler):
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, password):
            return self.return_json(status=401,
                                    msg="Wrong Password punk")  # if user doesn't exist or password is wrong, reload the page

            # if the above check passes, then we know the user has the right credentials
        if login_user(user):
            return self.return_json(status=200, msg="Logged in successfully")


class TestHandler(BaseHandler):
    @login_required
    def get(self):
        return self.return_json(status=200, msg='ok')


class LogoutHandler(BaseHandler):
    @login_required
    def post(self):
        try:
            logout_user()
            return self.return_json(status=200, msg='User successfully logged out')
        except:
            return self.return_json(status=200, msg='Session does not exist')


class CommentHandler(BaseHandler):
    @login_required
    def post(self):
        email = request.form.get('email')
        comment = request.form.get('comment')

        if not comment:
            return self.return_json(status='400', msg="Comment is empty")

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_comment = CommentSchema().load({'email': email,
                                            'comment': comment
                                            }).data

        # add the new user to the database
        db.session.add(new_comment)
        db.session.commit()

        return self.return_json(status=200, msg="New Comment Added")

    @login_required
    def get(self):
        try:
            comment = Comment.query.order_by(desc(Comment.created_on)).all()
            data = CommentSchema(many=True).dump(comment).data

            return self.return_json(msg=data)
        except DataError as e:
            return self.return_json(status=400, msg="Data error")
        except NoResultFound as e:
            return self.return_json(status=400, msg=str(e))
        except Exception as e:
            return self.return_json(status=400, msg=str(e))
