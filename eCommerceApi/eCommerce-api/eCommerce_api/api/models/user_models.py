from flask_restx import fields

from eCommerce_api.api.v1 import api

user = api.model('User', {
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

login_input = api.model('LoginInput', {
    'name' : fields.String(required=True, description='The user name'),
    'password' : fields.String(required=True, description='The user password')})

login_output = api.model('LoginOutput', {
    'token' : fields.String(required=True, description='The user was logged'),
    'message' : fields.String(required=True, description='User logged message')})

getUser_input = api.model('GetUserInput', {
    'name' : fields.String(required=True, description='The user name'),
    'password' : fields.String(required=True, description='The user password')})

getUser_output = api.model('GetUserOutput', {
    'user' : fields.Nested(user, required=True, description='The user information'),
    'message' : fields.String(required=True, description='User retrieved message')})