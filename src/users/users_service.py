from src.dto.register_users import RegisterUserDto
from src.dto.login_users import LoginUserDto
from users.users_repo import UsersRepository
from utils.pwd_hash import generate_password_hash
from utils.jwt_helper import generate_jwt
from utils.pwd_hash import check_password
from src.utils.schemas import UsersDetails
from exceptions.custom_exceptions import NotFoundException, BadRequestException

class UsersService:
    def __init__(self, session):
        self.session = session
        self.users_repository = UsersRepository(session)

    def register_user(self, dto: RegisterUserDto):
        try:
            with self.session.begin():
            
                # Check if email already exists
                existing_user = self.users_repository.get_user_by_email(dto.email)
                if existing_user:
                    raise BadRequestException(f"Email {dto} already exists")
                
                # Generate Password Hash
                password_hash = generate_password_hash(dto.password)
            
                # Register New User
                user = self.users_repository.create_user({
                    "fname": dto.fname,
                    "lname": dto.lname,
                    "email": dto.email,
                    "hash_password": password_hash
                })

            # Generate and return JWT token
            payload = {
                "id": user.id,
                "email": user.email
            }

            # Return the Generated JWT
            return generate_jwt(payload=payload)
        except Exception as e:
            raise e        

    def login_user(self, dto: LoginUserDto):
        try:
            # Check the User
            user = self.users_repository.get_user_by_email(dto.email)
            if not user:
                raise NotFoundException("User not found")
            
            # Check the Password
            if not check_password(user.password, dto.password):
                raise BadRequestException("Invalid email or password")

            # Generate and return JWT token
            payload = {
                "id": user.id,
                "email": user.email
            }

            return generate_jwt(payload=payload)
        except Exception as e:
            raise e
    
    def get_user_details(self, filters: dict):
        try:
            user = self.users_repository.get_user_by_filters(filters=filters)

            if not user:
                raise NotFoundException("User doesn't exists")
            
            return UsersDetails(
                id = user.id,
                email = user.email,
                name = f"{user.fname} {user.lname}"
            )
        except Exception as e:
            raise e