from .jwt_handler import JWTHandler

def test_jwt_handler():
    jwt_handler = JWTHandler()
    body = {
        "username": "test",
        "password": "test_password"
    }
    
    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)
    
    assert token is not None
    assert isinstance(token, str)
    assert token_information['username'] == body['username']