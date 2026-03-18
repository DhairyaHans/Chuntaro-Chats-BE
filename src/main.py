from fastapi import FastAPI
from auth.auth_controller import auth_v1_router
from users.users_controller import users_v1_router
from groups.groups_controller import groups_v1_router
from exceptions.custom_exceptions import AppException
from exceptions.handlers import app_exception_handler, generic_exception_handler

app = FastAPI(title="Chuntaro-Chats", version="1.0.0")

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(auth_v1_router, prefix="/api/v1")
app.include_router(users_v1_router, prefix="/api/v1")
app.include_router(groups_v1_router, prefix="/api/v1")
