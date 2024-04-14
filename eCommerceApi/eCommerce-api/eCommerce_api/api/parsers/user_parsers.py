from flask_restx import reqparse, inputs

authenticate_user_parser = reqparse.RequestParser()
authenticate_user_parser.add_argument('name', type=str, required=True, help='User name')
authenticate_user_parser.add_argument('password', type=str, required=True, help='User password')

add_user_parser = reqparse.RequestParser()
add_user_parser.add_argument('name', type=str, required=True, help='User name', location='json')
add_user_parser.add_argument('password', type=str, required=True, help='User password', location='json')

login_parser = reqparse.RequestParser()
login_parser.add_argument('name', type=str, required=True, help='User name', location='json')
login_parser.add_argument('password', type=str, required=True, help='User password', location='json')

getUser_parser = reqparse.RequestParser()
getUser_parser.add_argument('name', type=str, required=True, help='User name', location='json')
getUser_parser.add_argument('password', type=str, required=True, help='User password', location='json')