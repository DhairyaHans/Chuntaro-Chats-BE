from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from middlewares.auth import JWTBearer
from dto.groups import CreateGroupDto, GroupResponse
from src.utils.logger import logger
from groups.groups_service import GroupsService
from src.utils.connection import get_session
from src.utils.schemas import SuccessResponse
from http import HTTPStatus

groups_v1_router = APIRouter(prefix="/groups", tags=["groups"])

@groups_v1_router.post("/group", dependencies=[Depends(JWTBearer())], response_model=SuccessResponse[GroupResponse])
async def create_group(create_group_dto: CreateGroupDto, session: Session = Depends(get_session)):
    logger.info(f"Creating group with name: {create_group_dto.groupName}")
    group_service = GroupsService(session)
    data = group_service.create_group(create_group_dto)
    group_data = GroupResponse.model_validate(data)
    return SuccessResponse(
        message="Group Created Successfully",
        data=group_data,
        status=HTTPStatus.CREATED,
        meta={"info": HTTPStatus.CREATED.phrase}
    )
