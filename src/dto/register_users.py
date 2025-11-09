from pydantic import BaseModel, Field, EmailStr, field_validator
import string

class RegistedUserDto(BaseModel):
    fname: str = Field(description="User first name", min_length=3, max_length=50) 
    lname: str = Field(description="User last name", min_length=3, max_length=50)
    email: EmailStr = Field(description="User email address")
    password: str = Field(exclude=True, description="User password")

    # @field_validator('password')
    # @classmethod
    # def validate_password_complexity(cls, value):
    #     if len(value) < 8:
    #         raise ValueError("Password must be at least 8 characters long.")
    #     if not any(c.isupper() for c in value):
    #         raise ValueError("Password must contain at least one uppercase letter.")
    #     if not any(c.islower() for c in value):
    #         raise ValueError("Password must contain at least one lowercase letter.")
    #     if not any(c.isdigit() for c in value):
    #         raise ValueError("Password must contain at least one digit.")
    #     if not any(c in string.punctuation for c in value):
    #         raise ValueError("Password must contain at least one special character.")
    #     return value