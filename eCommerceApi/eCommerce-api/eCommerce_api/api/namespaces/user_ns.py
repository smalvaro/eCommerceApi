import flask
import datetime
from time import sleep

import json
from flask_restx import Resource
from flask import request

from eCommerce_api import logger
from eCommerce_api.api.v1 import api
from eCommerce_api.core import cache, limiter
from eCommerce_api.utils import handle400error, handle404error, handle500error

from eCommerce_api.api.models.user_models import authenticate_user_input, authenticate_user_output, add_user_input, add_user_output, login_input, login_output
from eCommerce_api.api.parsers.user_parsers import delete_fabricante_parser, add_fabricante_parser, authenticate_user_parser, add_user_parser, login_parser
from eCommerce_api.model.user_model import UserModel


userModel = UserModel()

user_ns= api.namespace('user', description='User operations')



@user_ns.route('/register')
class AddUser(Resource):
    @api.expect(add_user_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(add_user_output)
    def post(self):
        global userModel
        try:
            params = add_user_parser.parse_args()    
        except Exception as e:
            return handle400error(user_ns, "Malformed request")
        
        try:
            success, message = userModel.add_user(params['name'], params['password'])
        except Exception as e:
                return handle500error(user_ns, "Internal server error")
            
        return {"added":success, "message": message}, 200
    
@user_ns.route('/login')
class Login(Resource):
    @api.expect(login_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(login_output)
    def post(self):
        global userModel
        try:
            params = login_parser.parse_args()    
        except Exception as e:
            return handle400error(user_ns, "Malformed request")
        
        try:
            token, message = userModel.login(params['name'], params['password'])
        except Exception as e:
                return handle500error(user_ns, "Internal server error"+ str(e))
            
        return {"token":token, "message": message}, 200