from database.groups import Groups
from database.groups_users import GroupsUsers
from utils.logger import logger

class GroupRepository:
    def __init__(self, session):
        self.session = session

    def create_group(self, group_data: dict) -> Groups:
        group = Groups(
            group_name=group_data["group_name"],
            description=group_data["description"],
            owner_id=group_data["owner_id"]
        )
        self.session.add(group)
        self.session.flush()
        self.session.refresh(group)
        return group

    def get_group_details(self, group_id: str) -> Groups:
        return self.session.query(Groups) \
            .filter(Groups.uuid == group_id) \
            .first()
    
    def add_users_to_group(self, group_id: str, users_list: list):
        groups_users_data = []
        for user in users_list:
            groups_users_data.append(
                GroupsUsers(
                    user_id=user["id"],
                    group_id=group_id,
                    is_admin=user.get("is_admin", False)
                )
            )
        self.session.add_all(groups_users_data)
        self.session.flush()
        return groups_users_data
    