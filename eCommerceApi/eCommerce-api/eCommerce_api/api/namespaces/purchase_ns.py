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
from eCommerce_api.api.models.purchase_models import addPurchase_input,addPurchase_output, getPurchases_output
from eCommerce_api.api.parsers.purchase_parsers import addPurchase_parser
from eCommerce_api.model.purchase_model import PurchaseModel
from eCommerce_api.model.user_model import token_required
purchaseModel= PurchaseModel()

purchase_ns = api.namespace('purchase', description='Purchase operations')
@purchase_ns.route('/makePurchase')
class AddPurchase(Resource):
        @api.expect(addPurchase_input)
        @api.response(404, 'Product not found')
        @api.response(500, 'Internal server error')
        @api.response(400, 'Bad request')
        @token_required
        @api.marshal_with(addPurchase_output)
        def post(self):
            global purchaseModel
            try:
                params = addPurchase_parser.parse_args()    
            except Exception as e:
                return handle400error(purchase_ns, "Malformed request")
            
            try:
                success, message = purchaseModel.purchase(params['product_id'], params['quantity'])
            except Exception as e:
                    return handle500error(purchase_ns, "Internal server error"+ str(e))
                
            return {"added":success, "message": message}, 200
        
@purchase_ns.route('/getPurchases')
class GetPurchases(Resource):
    @api.response(500, 'Internal server error')
    @token_required
    @api.marshal_with(getPurchases_output)
    def get(self):
        global purchaseModel
        try:
            purchases, message = purchaseModel.get_purchases()
        except Exception as e:
            return handle500error(purchase_ns, "Internal server error")
        
        return {"purchases":purchases, "message": message}, 200
        