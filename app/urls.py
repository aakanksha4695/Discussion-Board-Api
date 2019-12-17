
from app import api
from app.handlers.authentication import LoginHandler
from app.handlers.authentication import SignupHandler
from app.handlers.base_handler import Ping
from app.handlers.authentication import TestHandler
from app.handlers.authentication import LogoutHandler
from  app.handlers.authentication import CommentHandler


api.add_resource(Ping, '/ping')
api.add_resource(SignupHandler, '/signup')
api.add_resource(LoginHandler, '/login')
api.add_resource(TestHandler, '/test-login')
api.add_resource(LogoutHandler, '/logout')
api.add_resource(CommentHandler, '/comment')
