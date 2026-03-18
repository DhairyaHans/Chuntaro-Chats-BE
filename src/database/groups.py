from sqlalchemy import Column, UUID, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base
import uuid

class Groups(Base):
    __tablename__ = "groups"
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_name = Column("name", String)
    description = Column("description", String)
    owner_id = Column("owner_id", Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column("updated_at", DateTime, default=datetime.now)
    
    owner = relationship("Users", back_populates="owned_groups")

    user_associations = relationship(
        "GroupsUsers",
        back_populates="group",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (f"<Group(uuid={self.uuid}, group_name={self.group_name}, owner_id={self.owner_id})>")

    def __str__(self) -> str:
        return f"Group_name={self.group_name}, created_at={self.created_at}"

    
