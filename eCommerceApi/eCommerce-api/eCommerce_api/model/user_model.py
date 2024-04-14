from functools import wraps
from typing import Any, Dict

from flask import request
import jwt
from eCommerce_api import config, logger

from eCommerce_api.model.db_model import PostgresSingleton
DENYLIST = set()
class ModelUser:
    name: str
    password: str
   
    def __init__(self,data: Dict[str, Any]) -> None:
        self.name = data[0]
        self.password = data[1]
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'password': self.password,
            }

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return None, f'No token provided !!'
        if token_in_denylist(token):
            return None, f'Token is in denylist !!'
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, config.SECRET_KEY, algorithms="HS256")
            #current_user,message = UserModel().getUser(data['name'], data['password'])
        except Exception as e:
            return None, f'Error generating token: {e}'
        # returns the current logged in users context to the routes
        return f(*args, **kwargs)
    return decorated
  
def token_in_denylist(token):
    return token in DENYLIST
  
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
       
    def getUser(self,name:str,password:str)->[Dict[str,Any]]:
        try:
            output = []
            query = "SELECT name,password FROM users WHERE name = %s AND password = %s"
            params = (name, password)
            self.dbSingleton.execute(query, params)
            result= self.dbSingleton.fetchOne()
            if result is None or len(result) == 0:
                return None, "User not found"
            else:
                output.append(ModelUser(result).to_dict())
                print(output)
                return output, "User found"
        except Exception as e:
            return None, f'Error getting user: {e}'