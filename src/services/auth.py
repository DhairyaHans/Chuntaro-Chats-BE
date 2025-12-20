from src.dto.register_users import RegisterUserDto
from src.dto.login_users import LoginUserDto
from src.services.users import UsersService
from utils.schemas import AuthResponse, SuccessResponse, ErrorResponse
from http import HTTPStatus

class AuthService:
    def __init__(self):
        self.user_service = UsersService()

    async def register_user(self, register_user_dto: RegisterUserDto) -> SuccessResponse[AuthResponse] | ErrorResponse:
        try:
            print("XX", register_user_dto)
            token = await self.user_service.register_user(register_user_dto)
            print("USER REGISTERED")
            data = AuthResponse(
                token=token
            )
            response = SuccessResponse[AuthResponse](
                message="User Registered Successfully",
                data=data,
                status=HTTPStatus.CREATED.value,
                meta={
                    "info": HTTPStatus.CREATED.description
                }
            )
            return response
        except Exception as e:
            error_message = str(e)
            response = ErrorResponse(
                error=error_message,
                status=HTTPStatus.BAD_REQUEST.value,
                meta={
                    "info": HTTPStatus.BAD_REQUEST.description
                }
            )
            return response

    async def login_user(self, login_user_dto: LoginUserDto) -> SuccessResponse[AuthResponse] | ErrorResponse:
        try:
            token = await self.user_service.login_user(login_user_dto)
            data = AuthResponse(
                token=token
            )
            response = SuccessResponse[AuthResponse](
                message="User Logged In Successfully",
                data=data,
                status=HTTPStatus.OK.value,
                meta={
                    "info": HTTPStatus.OK.description
                }
            )
            return response
        except Exception as e:
            error_message = str(e)
            response = ErrorResponse(
                error=error_message,
                status=HTTPStatus.BAD_REQUEST.value,
                meta={
                    "info": HTTPStatus.BAD_REQUEST.description
                }
            )
            return response