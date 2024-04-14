from typing import Any, Dict

from eCommerce_api import config, logger

from eCommerce_api.model.db_model import PostgresSingleton



class ModelProduct:
    product_id: int
    product_name: str
    price: float
    quantity: int
    
    def __init__(self,data: Dict[str, Any]) -> None:
        self.product_id = data[0]
        self.product_name = data[1]
        self.price = data[2]
        self.quantity = data[3]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'price': self.price,
            'quantity': self.quantity
        }
        
class InventoryModel:
    def __init__(self) -> None:
        self.dbSingleton = PostgresSingleton.getInstance()
        self.dbSingleton.connect()
        
    def add_product(self, product_id: int, product_name: str, price: float, quantity: int) ->[bool,str]:
        try:
            query = "INSERT INTO product (product_id, product_name, price, quantity) VALUES (%s, %s, %s, %s)"
            params = (product_id, product_name, price, quantity,)
            self.dbSingleton.execute(query, params)
            return True, "Product added"
        except Exception as e:
            return False, f'Error adding product: {e}'
        
    def get_products(self) ->[Dict[str, Any], str]:
        try:
            output = []
            query = "SELECT * FROM product"
            params = ()
            self.dbSingleton.execute(query, params)
            result= self.dbSingleton.fetchAll()
            
            for product in result:
                output.append(ModelProduct(product).to_dict())
            
            if result is None:
                return None, "No products found"
            else:
                return output, "Products found"
        except Exception as e:
            return None, f'Error getting products: {e}'  
    
    def update_product(self, product_id: int, product_name: str, price: float, quantity: int) -> [bool,str]:
        try:
            query = "UPDATE product SET product_name = %s, price = %s, quantity = %s WHERE product_id = %s"
            params = (product_name, price, quantity, product_id)
            self.dbSingleton.execute(query, params)
            return True, "Product updated"
        except Exception as e:
            return False, f'Error updating product: {e}'
        
    