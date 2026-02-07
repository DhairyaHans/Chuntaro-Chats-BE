from fastapi import APIRouter, Depends
from middlewares.auth import JWTBearer
from dto.groups import CreateGroupDto
from src.utils.logger import logger

group_router = APIRouter()

@group_router.post("/group", dependencies=[Depends(JWTBearer())],  tags=["groups"])
async def create_group(create_group_dto: CreateGroupDto):
    