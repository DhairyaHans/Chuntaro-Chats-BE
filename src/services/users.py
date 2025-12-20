from src.dto.register_users import RegisterUserDto
from src.dto.login_users import LoginUserDto
from src.repositories.users import UsersRepository
from utils.pwd_hash import generate_password_hash
from utils.jwt_helper import generate_jwt
from utils.schemas import SuccessResponse, ErrorResponse, UsersDetails
from http import HTTPStatus

class UsersService:
    def __init__(self):
        self.users_repository = UsersRepository()

    async def register_user(self, register_user_dto: RegisterUserDto):
        print("ashlkdhaslk")
        try:
            # Generate Password Hash
            print("rasdlahdlha", register_user_dto)
            password_hash = generate_password_hash(register_user_dto.password)
            register_user_dto.password = password_hash
            
            # Check if email already exists
            is_exists = self.get_user_details({"email": register_user_dto.email})
            if is_exists:
                raise ValueError(f"Email {register_user_dto.email} already exists")

            print("REGIHSLDHALHD")
            # Register New User
            user = await self.users_repository.register_user(register_user_dto=register_user_dto)

            # Generate and return JWT token
            print("ksadhkjashdkjh")
            payload = {
                "id": user.id,
                "email": user.email
            }
            print("xaksdhashdksahdlk", payload)
            token = generate_jwt(payload=payload)
            print("JWT-  ", token)
            return token
        except Exception as e:
            raise e        

    async def login_user(self, login_user_dto: LoginUserDto):
        try:
            # Login the User
            user = await self.users_repository.login_user(login_user_dto=login_user_dto)
            
            # Generate and return JWT token
            payload = {
                "id": user.id,
                "email": user.email
            }
            token = generate_jwt(payload=payload)
            return token
        except Exception as e:
            raise e
    
    async def get_user_details(self, id):
        try:
            user = await self.users_repository.get_user_details({"id": id})
            if not user:
                raise Exception(f"User with id {id} doesn't exists")
            else:
                print("User by id - ", id, ' - ', user)
                user_details = UsersDetails(
                    id = user.id,
                    email = user.email,
                    name = f"{user.fname} {user.lname}"
                )

                response = SuccessResponse[UsersDetails](
                    message="User Registered Successfully",
                    data=user_details,
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