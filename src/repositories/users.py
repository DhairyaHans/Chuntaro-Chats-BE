from src.database.users import Users
from src.dto.register_users import RegisterUserDto
from src.dto.login_users import LoginUserDto
from utils.connection import  get_session
from utils.pwd_hash import check_password

class UsersRepository:
    async def register_user(self, register_user_dto: RegisterUserDto) -> Users:
        with get_session() as session:
            try:
                print("fname = ",register_user_dto.fname)
                print("lname = ",register_user_dto.lname)
                print("email = ",register_user_dto.email)
                print("password = ",register_user_dto.password)
                user_data = Users(
                    fname = register_user_dto.fname,
                    lname = register_user_dto.lname,
                    email = register_user_dto.email,
                    password = register_user_dto.password
                )
                print("user- ", user_data)
                session.add(user_data)
                session.commit()
                print("user added")
                session.refresh(user_data)  # Ensure the instance is bound to the session
                return user_data
            except Exception as e:
                session.rollback()
                raise e
            
    async def login_user(self, login_user_dto: LoginUserDto) -> Users:
        try:
            user = await self.get_user_details({"email": login_user_dto.email})
            if not user:
                raise Exception("User not found")
            if not check_password(user.password, login_user_dto.password):
                raise Exception("Invalid email or password")
            return user
        except Exception as e:
            raise e

    async def get_user_details(self, filters: dict) -> Users:
        user = None
        print("filters in repo - ", filters)
        with get_session() as session:
            print("jsdlkashdlhas")
            query = session.query(Users)
            print(filters)
            for key, value in filters.items():
                print(key, value)
                if key == 'email':
                    query = query.filter(
                        Users.email==value
                    )        
                if key == 'id':
                    query = query.filter(
                        Users.id==value
                    )
                if key == 'fname':
                    query = query.filter(
                        Users.fname.ilike(value)
                    )
                if key == 'lname':
                    query = query.filter(
                        Users.lname.ilike(value)
                    )
            print("query - ", query)
            user = query.first()
            print("user fetched - ", user)
        return user
