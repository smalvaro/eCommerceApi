from typing import Any, Dict

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
        self.dbSingleton = PostgresSingleton.get_instance()
        self.dbSingleton.connect()
        
    def get_user(self, name: str,password : str) ->[Dict[str, Any], str]:
        try:
            
            output = []
            
            query = "SELECT * FROM users WHERE name = %s and password = %s"
            params = (name, password,)
            self.dbSingleton.execute(query, params)
            result = self.dbSingleton.fetchOne()
            
            output.append(ModelUser(result).to_dict())
            
            if result is None:
                return None, "User not found"
            else:
                return output, "User found"
        except Exception as e:
            return None,f'Error getting user: {e}'
        
    #I am going to put the funtion that authenticates the user via JWT and the database here
    #I will also put the function that creates a new user here
    def add_user(self, name: str, password: str) -> None:
        try:
            query= "INSERT INTO users (name, password) VALUES (%s, %s)"
            params= (name, password)
            self.dbSingleton.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
            
            return True,"User added succesfully"
        except Exception as e:
            return False,f'Error adding user: {e}'
        
    def authenticate_user(self, name: str, password: str) -> [Dict[str,Any],str]:
        try:
            query = "SELECT * FROM users WHERE name = %s AND password = %s"
            params = (name, password)
            self.dbSingleton.execute(query, params)
            result= self.dbSingleton.fetchOne()
            
            if result is None or len(result) == 0:
                return None, "User not found"
            else :
                return {"name": result[1], "password": result[2]}, "User found"
        
        except Exception as e:
            f'Error authenticating user: {e}'