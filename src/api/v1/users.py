from fastapi import APIRouter
from src.utils.logger import logger

users_router = APIRouter()

@users_router.get("/{id}")
async def get_user(id: int):
    # Fetch user data from db
    logger.info(f"Fetching user data with id: {id}")
    return {"user_id": id}
