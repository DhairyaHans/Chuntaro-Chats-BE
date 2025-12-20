import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt

load_dotenv()

def jwt_get_expiry_at():
    JWT_EXPIRATION_TIME = float(os.getenv("JWT_EXPIRATION_TIME"))
    return datetime.now() + timedelta(minutes=JWT_EXPIRATION_TIME)

def generate_jwt(payload: dict) -> str:
    JWT_SECRET = os.getenv("JWT_SECRET")
    ALGORITHM = os.getenv("JWT_HASHING_ALGO")
    expiry_at = jwt_get_expiry_at()
    payload["exp"] = expiry_at
    token = jwt.encode(payload, JWT_SECRET, ALGORITHM)
    return token

def get_token_payload(token: str) -> dict:
    JWT_SECRET = os.getenv("JWT_SECRET",)
    ALGORITHM = os.getenv("JWT_HASHING_ALGO")
    try:
        decoded_payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        print(decoded_payload)
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
        raise Exception("Invalid token")
    
def verify_token(token: str) -> dict:
    JWT_SECRET = os.getenv("JWT_SECRET",)
    ALGORITHM = os.getenv("JWT_HASHING_ALGO")
    is_token_valid = False
    try:
        decoded_payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except:
        decoded_payload = None
    print(decoded_payload)
    if decoded_payload:
        is_token_valid = True
    return is_token_valid
