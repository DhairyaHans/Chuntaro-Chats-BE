import bcrypt

def generate_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(pwd_bytes, salt)
    return password_hash

def check_password(password_hash: str, password: str) -> bool:
    print("passdkashdk - ", password)
    pwd_bytes = password.encode('utf-8')
    print("dhaskdhasi - ", pwd_bytes)
    return bcrypt.checkpw(pwd_bytes, password_hash)