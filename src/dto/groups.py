from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CreateGroupDto(BaseModel):
    groupName: str
    description: str | None = None
    ownerId: int

class UpdateGroupUsers(BaseModel):
    groupId: str
    usersList: list[int]

class UserEntry(BaseModel):
    userId: str
    isAdmin: bool

class GroupResponse(BaseModel):
    uuid: UUID
    group_name: str
    description: str | None
    owner_id: int
    created_at: datetime | None

    class Config:
        from_attributes = True