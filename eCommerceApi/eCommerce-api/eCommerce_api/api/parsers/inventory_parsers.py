from flask_restx import reqparse, inputs

addProduct_parser = reqparse.RequestParser()
addProduct_parser.add_argument('product_id', type=int, required=True, help='The product identifier')
addProduct_parser.add_argument('product_name', type=str, required=True, help='The product name')
addProduct_parser.add_argument('price', type=float, required=True, help='The product price')
addProduct_parser.add_argument('quantity', type=int, required=True, help='The product quantity')

updateProduct_parser = reqparse.RequestParser()
updateProduct_parser.add_argument('product_id', type=int, required=True, help='The product identifier')
updateProduct_parser.add_argument('product_name', type=str, required=True, help='The product name')
updateProduct_parser.add_argument('price', type=float, required=True, help='The product price')
updateProduct_parser.add_argument('quantity', type=int, required=True, help='The product quantity')
