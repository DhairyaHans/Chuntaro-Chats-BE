from src.database.users import Users

class UsersRepository:
    def __init__(self, session):
        self.session = session
        
    def create_user(self, user_data: dict) -> Users:
        user = Users(
            fname = user_data["fname"],
            lname = user_data["lname"],
            email = user_data["email"],
            password = user_data["hash_password"]
        )
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)  # Ensure the instance is bound to the session
        return user

    def get_user_by_email(self, email: str) -> Users | None:
        return self.session.query(Users) \
            .filter(Users.email == email) \
            .first()

    def get_user_by_filters(self, filters: dict) -> Users | None:
        query = self.session.query(Users)

        if "email" in filters:
            query = query.filter(Users.email == filters["email"])

        if "id" in filters:
            query = query.filter(Users.id == filters["id"])

        if "fname" in filters:
            query = query.filter(Users.fname.ilike(filters["fname"]))

        if "lname" in filters:
            query = query.filter(Users.lname.ilike(filters["lname"]))
        
        return query.first()
        
