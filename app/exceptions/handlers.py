from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import (
    BadRequestException,
    ConflictException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(BadRequestException)
    async def bad_request(_, exc):
        return JSONResponse(
            status_code=400,
            content={"detail": exc.message},
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized(_, exc):
        return JSONResponse(
            status_code=401,
            content={"detail": exc.message},
        )

    @app.exception_handler(ForbiddenException)
    async def forbidden(_, exc):
        return JSONResponse(
            status_code=403,
            content={"detail": exc.message},
        )

    @app.exception_handler(NotFoundException)
    async def not_found(_, exc):
        return JSONResponse(
            status_code=404,
            content={"detail": exc.message},
        )

    @app.exception_handler(ConflictException)
    async def conflict(_, exc):
        return JSONResponse(
            status_code=409,
            content={"detail": exc.message},
        )