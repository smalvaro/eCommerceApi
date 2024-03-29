import datetime
from typing import Any, Dict

from eCommerce_api import config, logger

from eCommerce_api.model.db_model import PostgresSingleton

class ModelPurchase:
    product_id: int
    quantity: int
    
    def __init__(self,data: Dict[str, Any]) -> None:
        self.product_id = data[0]
        self.quantity = data[1]
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'product_id': self.product_id,
            'quantity': self.quantity
        }


class PurchaseModel:
    def __init__(self) -> None:
        self.dbSingleton = PostgresSingleton.getInstance()
        self.dbSingleton.connect()
        
    def purchase(self, product_id: int, quantity: int) -> [Dict[str, Any], str]:
        try:
            #output = []
            
            query = "SELECT * FROM product WHERE product_id = %s"
            params = (product_id,)
            self.dbSingleton.execute(query, params)
            result = self.dbSingleton.fetchOne()
            
            if result is None:
                return None, "Product not found"
            
            if result[3] < quantity:
                return None, "Not enough stock"
            
            
            
            query = "UPDATE product SET quantity = quantity - %s WHERE product_id = %s"
            params = (quantity, product_id)
            self.dbSingleton.execute(query, params)
            
            query = "INSERT INTO purchase (product_id, quantity) VALUES (%s, %s)"
            params = (product_id, quantity)
            self.dbSingleton.execute(query, params)
            

            date = datetime.datetime.now(),
            
            #insert into my tabla recibo the data that you consider useful, for example the product_id, the quantity, the date, etc.
            query = "INSERT INTO recibo (product_id, quantity, date) VALUES (%s, %s, %s)"
            params = (product_id, quantity, date)
            self.dbSingleton.execute(query, params)
            
            #output.append(ModelPurchase(result).to_dict())
            
            return True, "Purchase successful"
        except Exception as e:
            return None, f'Error purchasing product: {e}'
        
    def get_purchases(self) -> [Dict[str, Any], str]:
        try:
            output = []
            query = "SELECT * FROM purchase"
            params = ()
            self.dbSingleton.execute(query, params)
            result = self.dbSingleton.fetchAll()
            
            for purchase in result:
                output.append(ModelPurchase(purchase).to_dict())
            
            if result is None:
                return None, "No purchases found"
            else:
                return output, "Purchases found"
        except Exception as e:
            return None, f'Error getting purchases: {e}'