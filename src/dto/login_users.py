from pydantic import BaseModel, Field, EmailStr

class LoginUserDto(BaseModel):
    email: EmailStr = Field(description="User email address")
    password: str = Field(exclude=True, description="User password")

    # def __dict__(self) -> dict:
    #     # safe serialization that never exposes the password
    #     return {
    #         "email": self.email,
    #     }
    
    # def __repr__(self) -> str:
    #     return f"LoginUserDto(email={self.email})"

    # def __str__(self) -> str:
        # return f"LoginUserDto with email: {self.email}"