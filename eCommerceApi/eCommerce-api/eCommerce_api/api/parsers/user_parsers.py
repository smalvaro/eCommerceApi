from flask_restx import reqparse, inputs

delete_fabricante_parser = reqparse.RequestParser()
delete_fabricante_parser.add_argument('id_fabricante', type=str, required=True, help='Fabricante ID')

add_fabricante_parser = reqparse.RequestParser()
add_fabricante_parser.add_argument('nombre', type=str, required=True, help='Fabricante name', location='json')
add_fabricante_parser.add_argument('logo', type=str, required=True, help='Fabricante logo', location='json')

authenticate_user_parser = reqparse.RequestParser()
authenticate_user_parser.add_argument('name', type=str, required=True, help='User name')
authenticate_user_parser.add_argument('password', type=str, required=True, help='User password')

add_user_parser = reqparse.RequestParser()
add_user_parser.add_argument('name', type=str, required=True, help='User name', location='json')
add_user_parser.add_argument('password', type=str, required=True, help='User password', location='json')

login_parser = reqparse.RequestParser()
login_parser.add_argument('name', type=str, required=True, help='User name', location='json')
login_parser.add_argument('password', type=str, required=True, help='User password', location='json')