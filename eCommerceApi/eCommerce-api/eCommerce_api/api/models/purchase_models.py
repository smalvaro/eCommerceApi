from flask_restx import fields

from eCommerce_api.api.v1 import api

purchase = api.model('Purchase', {
    'product_id' : fields.Integer(required=True, description='The product identifier'),
    'quantity' : fields.Integer(required=True, description='The product quantity')})

addPurchase_input = api.model('AddInput', {
    'product_id' : fields.Integer(required=True, description='The product identifier'),
    'quantity' : fields.Integer(required=True, description='The product quantity')})

addPurchase_output = api.model('AddOutput', {
    'added' : fields.Boolean(required=True, description='The purchase was added'),
    'message' : fields.String(required=True, description='Purchase added message')})

getPurchases_output = api.model('GetOutput', {
    'purchases' : fields.List(fields.Nested(purchase), required=True, description='The list of purchases'),
     'message' : fields.String(required=True, description='Purchase added message')})