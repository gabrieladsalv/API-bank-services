from flask import request
from src.drivers.jwt_handler import JWTHandler

def auth_jwt_verify():
    jwt_handle = JWTHandler()
    raw_token = request.headers.get('Authorization')
    user_id = request.headers.get('uid')
    
    if not raw_token or not user_id:
        raise Exception('Invalid Auth Information')
    
    token = raw_token.split()[1]
    token_information = jwt_handle.decode_token(token)
    token_uid = token_information['user_id']
    
    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information
    
    raise Exception('Unauthorized')