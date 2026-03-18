from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dto.login_users import LoginUserDto
from src.dto.register_users import RegisterUserDto
from users.users_service import UsersService
from src.utils.logger import logger
from src.utils.connection import get_session
from src.utils.schemas import SuccessResponse
from http import HTTPStatus

auth_v1_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_v1_router.post("/register")
def register_user(register_user_dto: RegisterUserDto, session: Session = Depends(get_session)):
    logger.info(f"Register User Data - {register_user_dto}")
    users_service = UsersService(session)
    token = users_service.register_user(register_user_dto)
    return SuccessResponse(
        message="User Registered Successfully",
        data={"token": token},
        status=HTTPStatus.CREATED,
        meta={"info": HTTPStatus.CREATED.phrase}
    )

@auth_v1_router.post("/login")
def login_user(login_user_dto: LoginUserDto, session: Session = Depends(get_session)):
    logger.info(f"Login User Data - {login_user_dto}")
    users_service = UsersService(session)
    token = users_service.login_user(login_user_dto)
    return SuccessResponse(
        message="User Login Successfully",
        data={"token": token},
        status=HTTPStatus.OK,
        meta={"info": HTTPStatus.OK.phrase}
    )