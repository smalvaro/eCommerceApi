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

from eCommerce_api.api.models.inventory_models import addProduct_input,addProduct_output,getProduct_output,updateProduct_input,updateProduct_output
from eCommerce_api.api.parsers.inventory_parsers import addProduct_parser,updateProduct_parser
from eCommerce_api.model.inventory_model import InventoryModel
from eCommerce_api.model.user_model import token_required

inventoryModel= InventoryModel()
inventory_ns= api.namespace('inventory', description='Inventory operations')

@inventory_ns.route('/addProduct')
class AddProduct(Resource):
    @api.expect(addProduct_input)
    @api.response(404, 'Product not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @token_required
    @api.marshal_with(addProduct_output)
    def post(self):
        global inventoryModel
        try:
            params = addProduct_parser.parse_args()    
        except Exception as e:
            return handle400error(inventory_ns, "Malformed request")
        
        try:
            success, message = inventoryModel.add_product(params['product_id'], params['product_name'], params['price'], params['quantity'])
        except Exception as e:
                return handle500error(inventory_ns, "Internal server error")
            
        return {"added":success, "message": message}, 200

@inventory_ns.route('/getProducts')
class GetProducts(Resource):
    @api.response(404, 'Products not found')
    @api.response(500, 'Internal server error')
    @api.response(400,'Bad request')
    @token_required
    @api.marshal_with(getProduct_output)
    def get(self):
        global inventoryModel
        try:
            products, message = inventoryModel.get_products()
        except Exception as e:
            return handle500error(inventory_ns, "Internal server error")
        
        return {"products":products, "message": message}, 200
    
@inventory_ns.route('/updateProduct')
class UpdateProduct(Resource):
    @api.expect(updateProduct_input)
    @api.response(404, 'Product not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @token_required
    @api.marshal_with(updateProduct_output)
    def post(self):
        global inventoryModel
        try:
            params = updateProduct_parser.parse_args()  
        except Exception as e:
            return handle400error(inventory_ns, "Malformed request")
        
        try:
            success, message = inventoryModel.update_product(params['product_id'], params['product_name'], params['price'], params['quantity'])
        except Exception as e:
                return handle500error(inventory_ns, "Internal server error")
            
        return {"updated":success, "message": message}, 200