from fastapi import APIRouter
from src.dto.login_users import LoginUserDto
from src.dto.register_users import RegistedUserDto
from src.utils.logger import logger

auth_router = APIRouter()

@auth_router.post("/register")
async def register_user(register_user_dto: RegistedUserDto):
    # Save user data to db
    logger.info(f"Register User Data - {register_user_dto}")
    return {"message": "User registered successfully"}

@auth_router.post("/login")
async def login_user(login_user_dto: LoginUserDto):
    # Check db, if the user data is correct or not
    logger.info(f"Login User Data - {login_user_dto}")
    return {"message": "User logged in successfully"}
                