from fastapi import FastAPI
from src.api.v1.auth import auth_router
from src.api.v1.users import users_router

app = FastAPI(title="Chuntaro-Chats", version="1.0.0")

app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
