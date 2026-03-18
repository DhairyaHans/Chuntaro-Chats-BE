from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.custom_exceptions import AppException
from utils.schemas import ErrorResponse
from http import HTTPStatus
from src.utils.logger import logger

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.message,
            status=exc.status_code,
            meta={"info": HTTPStatus(exc.status_code).description}
        ).model_dump()
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal Server Error",
            status=500,
            meta={"info": "Something went wrong"}
        ).model_dump()
    )