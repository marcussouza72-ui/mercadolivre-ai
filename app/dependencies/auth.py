from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.jwt import decode_token
from app.dependencies.repositories import get_user_repository
from app.exceptions.exceptions import (
    NotFoundException,
    UnauthorizedException,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    repository: UserRepository = Depends(get_user_repository),
) -> User:

    token = credentials.credentials

    payload = decode_token(token)

    if payload.type != "access":
        raise UnauthorizedException("Token inválido.")

    try:
        user_id = UUID(payload.sub)
    except (ValueError, TypeError):
        raise UnauthorizedException("Token inválido.")

    user = await repository.get_by_id(user_id)

    if user is None:
        raise NotFoundException("Usuário não encontrado.")

    if not user.is_active:
        raise UnauthorizedException("Usuário inativo.")

    return user