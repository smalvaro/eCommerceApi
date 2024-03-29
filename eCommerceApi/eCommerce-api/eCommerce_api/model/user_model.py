from typing import Any, Dict
import jwt
from eCommerce_api import config, logger

from eCommerce_api.model.db_model import PostgresSingleton
class ModelUser:
    name: str
    password: str
    
    def __init__(self,data: Dict[str, Any]) -> None:
        self.name = data[0]
        self.password = data[1]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'nombre': self.nombre,
            'logo': self.logo
        }
    
class UserModel:
    def __init__(self) -> None:
        self.dbSingleton = PostgresSingleton.getInstance()
        self.dbSingleton.connect()
        

    def add_user(self, name: str, password: str) -> None:
        try:
            query= "INSERT INTO users (name, password) VALUES (%s, %s)"
            params= (name, password)
            self.dbSingleton.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
            
            return True,"User added succesfully"
        except Exception as e:
            return False,f'Error adding user: {e}'
        
    
    #make a function where, given the name and password of the user it generates a jwt token to authenticate the user
    def login(self, name: str, password: str) -> [Dict[str,Any],str]:
        try:
            query = "SELECT * FROM users WHERE name = %s AND password = %s"
            params = (name, password)
            self.dbSingleton.execute(query, params)
            result= self.dbSingleton.fetchOne()
            
            if result is None or len(result) == 0:
                return None, "User not found"
            else :
                token = jwt.encode({"name": name, "password": password}, config.SECRET_KEY, algorithm="HS256")
                
                return {"token": token}, "Token generated"
        
        except Exception as e:
           return None, f'Error generating token: {e}'