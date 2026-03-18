from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.base import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now) 

    owned_groups = relationship("Groups", back_populates="owner")

    group_associations = relationship(
        "GroupsUsers",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (f"<Users(id={self.id}, fname='{self.fname}', lname='{self.lname}', "
                f"email='{self.email}', created_at={self.created_at})>")

    def __str__(self) -> str:
        return (f"User {self.id}: {self.fname} {self.lname} ({self.email})")
