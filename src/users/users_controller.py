from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.logger import logger
from middlewares.auth import JWTBearer
from users.users_service import UsersService
from src.utils.connection import get_session
from utils.schemas import SuccessResponse, ErrorResponse
from http import HTTPStatus
from src.dto.users import UserResponse

users_v1_router = APIRouter(prefix="/users", tags=["users"])

@users_v1_router.get("/{id}", dependencies=[Depends(JWTBearer())])
async def get_user(id: int, session: Session = Depends(get_session), response_model=SuccessResponse[UserResponse]):
    user_service = UsersService(session)
    data = user_service.get_user_details({"id": id})
    user_data = UserResponse.model_validate(data)
    return SuccessResponse(
        message="User fetched successfully",
        data=user_data,
        status=HTTPStatus.OK.value,
        meta={"info": HTTPStatus.OK.phrase}
    )