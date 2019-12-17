import logging

from flask_restful import Resource
from flask import request
from app import db
from app import flask_app
from app.config import Config
from flask import g

logger = logging.getLogger(__name__)

class BaseHandler(Resource):

    def return_json(self, status=200, msg="Success"):
        return {"status": status, "msg": msg}, status


class Ping(BaseHandler):

    def get(self):
        return self.return_json()
