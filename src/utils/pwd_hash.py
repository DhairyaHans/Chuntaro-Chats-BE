import bcrypt

def generate_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(pwd_bytes, salt)
    generated_password = password_hash.decode('utf-8')
    return generated_password

def check_password(password_hash: str, password: str) -> bool:
    pwd_bytes = password.encode('utf-8')
    password_hash_bytes = password_hash.encode('utf-8')
    return bcrypt.checkpw(pwd_bytes, password_hash_bytes)