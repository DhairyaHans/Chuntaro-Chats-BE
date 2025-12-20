from fastapi import APIRouter
from src.dto.login_users import LoginUserDto
from src.dto.register_users import RegisterUserDto
from src.services.auth import AuthService
from src.utils.logger import logger

auth_router = APIRouter()

@auth_router.post("/register", tags=["auth"])
async def register_user(register_user_dto: RegisterUserDto):
    # Save user data to db
    logger.info(f"Register User Data - {register_user_dto}")
    auth_service = AuthService()
    print("aiusfdjsdlj")
    response = await auth_service.register_user(register_user_dto=register_user_dto)
    return response

@auth_router.post("/login", tags=["auth"])
async def login_user(login_user_dto: LoginUserDto):
    # Check db, if the user data is correct or not
    logger.info(f"Login User Data - {login_user_dto}")
    auth_service = AuthService()
    response = await auth_service.login_user(login_user_dto=login_user_dto)
    return response
                