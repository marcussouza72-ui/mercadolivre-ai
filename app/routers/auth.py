from fastapi import APIRouter, Depends, status

from app.dependencies.auth import get_current_user
from app.dependencies.services import get_user_service
from app.models.user import User
from app.schemas.user import (
    RefreshTokenRequest,
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return await service.create_user(data)


@router.post(
    "/login",
    response_model=Token,
)
async def login(
    data: UserLogin,
    service: UserService = Depends(get_user_service),
):
    return await service.authenticate(
        data.email,
        data.password,
    )


@router.post(
    "/refresh",
    response_model=Token,
)
async def refresh(
    data: RefreshTokenRequest,
    service: UserService = Depends(get_user_service),
):
    return await service.refresh_token(
        data.refresh_token,
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
async def me(
    current_user: User = Depends(get_current_user),
):
    return current_user