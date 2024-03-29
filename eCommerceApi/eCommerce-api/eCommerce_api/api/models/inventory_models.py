from flask_restx import fields

from eCommerce_api.api.v1 import api

product = api.model('Product', {
    'product_id' : fields.Integer(required=True, description='The product identifier'),
    'product_name' : fields.String(required=True, description='The product name'),
    'price' : fields.Float(required=True, description='The product price'),
    'quantity' : fields.Integer(required=True, description='The product quantity')})

addProduct_input = api.model('AddInput', {
    'product_id' : fields.Integer(required=True, description='The product identifier'),
    'product_name' : fields.String(required=True, description='The product name'),
    'price' : fields.Float(required=True, description='The product price'),
    'quantity' : fields.Integer(required=True, description='The product quantity')})
    
addProduct_output = api.model('AddOutput', {
    'added' : fields.Boolean(required=True, description='The product was added'),
    'message' : fields.String(required=True, description='Product added message')})

getProduct_output = api.model('GetOutput', {
    'product' : fields.List(fields.Nested(product), required=True, description='The product list'),
    'message' : fields.String(required=True, description='Product list message')})

updateProduct_input = api.model('UpdateInput', {
    'product_id' : fields.Integer(required=True, description='The product identifier'),
    'product_name' : fields.String(required=True, description='The product name'),
    'price' : fields.Float(required=True, description='The product price'),
    'quantity' : fields.Integer(required=True, description='The product quantity')})

updateProduct_output = api.model('UpdateOutput', {
    'updated' : fields.Boolean(required=True, description='The product was updated'),
    'message' : fields.String(required=True, description='Product updated message')})