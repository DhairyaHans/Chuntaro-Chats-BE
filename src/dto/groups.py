from pydantic import BaseModel

class CreateGroupDto(BaseModel):
    userIds: list[int]
    groupName: str
    temp: bool = False
    adminIds: list[int]
    description: str | None = None