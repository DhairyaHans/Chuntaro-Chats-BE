from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now()) 
    
    # def __dict__(self) -> dict:
    #     # safe serialization that never exposes the password
    #     return {
    #         "id": self.id,
    #         "fname": self.fname,
    #         "lname": self.lname,
    #         "email": self.email,
    #         "created_at": self.created_at.isoformat() if self.created_at else None,
    #     }

    # def __repr__(self) -> dict:
    #     return (f"<Users(id={self.id}, fname='{self.fname}', lname='{self.lname}', "
    #             f"email='{self.email}', created_at={self.created_at})>")

    # def __str__(self) -> dict:
    #     return (f"User {self.id}: {self.fname} {self.lname} ({self.email})")
