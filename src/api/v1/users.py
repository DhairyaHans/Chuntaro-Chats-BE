from fastapi import APIRouter, Depends
from src.utils.logger import logger
from middlewares.auth import JWTBearer
from services.users import UsersService

users_router = APIRouter()

@users_router.get("/{id}", dependencies=[Depends(JWTBearer())], tags=["users"])
async def get_user(id: int):
    # Fetch user data from db
    logger.info(f"Fetching user data with id: {id}")
    user_service = UsersService()
    print({"id": id})
    response = await user_service.get_user_details({"id": id})
    return response
