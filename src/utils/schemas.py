from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    message: str
    data: T
    status: int
    meta: dict

class ErrorResponse(BaseModel):
    error: str
    status: int
    meta: dict

class AuthResponse(BaseModel):
    token: str

class UsersDetails(BaseModel):
    id: int
    email: str
    name: str

