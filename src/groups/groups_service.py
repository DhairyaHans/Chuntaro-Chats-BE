from dto.groups import CreateGroupDto
from groups.groups_repo import GroupRepository
from utils.logger import logger
from utils.schemas import SuccessResponse, ErrorResponse
from http import HTTPStatus

class GroupsService:
    def __init__(self, session):
        self.session = session
        self.group_repo = GroupRepository(session)

    def create_group(self, dto: CreateGroupDto):
        try:
            with self.session.begin():
                group = self.group_repo.create_group({
                    "group_name": dto.groupName,
                    "description": dto.description,
                    "owner_id": dto.ownerId
                })
                print("GROUP - ", group)
                users_list = [{
                    "id": dto.ownerId,
                    "is_admin": True
                }]
                self.group_repo.add_users_to_group(
                    group.uuid,
                    users_list
                )
            return group
        except Exception as e:
            logger.error(f"Error occurred while creating group - {str(e)}")
            raise Exception(f"Error while creating the group - {dto.groupName}")