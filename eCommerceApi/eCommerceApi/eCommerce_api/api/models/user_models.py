from flask_restx import fields

from eCommerce_api.api.v1 import api

user = api.model('User', {
    'id' : fields.String(required=True, description='The user identifier'),
    'name' : fields.String(required=True, description='The user name'),
    'password' : fields.String(required=True, description='The user password')})

authenticate_user_input = api.model('AuthenticateUserInput', {
    'name' : fields.String(required=True, description='The user name'),
    'password' : fields.String(required=True, description='The user password')})

authenticate_user_output = api.model('AuthenticateUserOutput', {
    'authenticated' : fields.Boolean(required=True, description='The user was authenticated'),
    'message' : fields.String(required=True, description='User authenticated message')})

add_user_input = api.model('AddUserInput', {
    'name' : fields.String(required=True, description='The user name'),
    'password' : fields.String(required=True, description='The user password')})

add_user_output = api.model('AddUserOutput', {
    'added' : fields.Boolean(required=True, description='The user was added'),
    'message' : fields.String(required=True, description='User added message')})