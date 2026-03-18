from sqlalchemy import Column, Integer, ForeignKey, UUID, Boolean, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database.base import Base
from datetime import datetime

class GroupsUsers(Base):
    __tablename__ = "groups_users"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.uuid"), nullable=False)
    is_admin = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=datetime.now)

    __table_args__ = (
        PrimaryKeyConstraint("group_id", "user_id"),
    )

    user = relationship("Users", back_populates="group_associations")
    group = relationship("Groups", back_populates="user_associations")