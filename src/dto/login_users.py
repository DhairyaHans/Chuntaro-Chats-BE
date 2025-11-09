from pydantic import BaseModel, Field, EmailStr

class LoginUserDto(BaseModel):
    email: EmailStr = Field(description="User email address")
    password: str = Field(exclude=True, description="User password")