from flask_restx import reqparse, inputs

addPurchase_parser = reqparse.RequestParser()
addPurchase_parser.add_argument('product_id', type=int, required=True, help='The product identifier')
addPurchase_parser.add_argument('quantity', type=int, required=True, help='The product quantity')