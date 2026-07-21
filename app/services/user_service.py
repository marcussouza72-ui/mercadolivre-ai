from uuid import UUID

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.exceptions.exceptions import (
    ConflictException,
    UnauthorizedException,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import Token, UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def _generate_tokens(self, user: User) -> Token:
        return Token(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def create_user(
        self,
        data: UserCreate,
    ) -> User:

        existing_user = await self.repository.get_by_email(
            data.email,
        )

        if existing_user:
            raise ConflictException(
                "E-mail já cadastrado."
            )

        user = User(
            name=data.name,
            email=data.email,
            password_hash=hash_password(data.password),
        )

        return await self.repository.create(user)

    async def authenticate(
        self,
        email: str,
        password: str,
    ) -> Token:

        user = await self.repository.get_by_email(
            email,
        )

        if user is None:
            raise UnauthorizedException(
                "Usuário ou senha inválidos."
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise UnauthorizedException(
                "Usuário ou senha inválidos."
            )

        if not user.is_active:
            raise UnauthorizedException(
                "Usuário inativo."
            )

        return self._generate_tokens(user)

    async def refresh_token(
        self,
        refresh_token: str,
    ) -> Token:

        payload = decode_token(refresh_token)

        if payload.type != "refresh":
            raise UnauthorizedException(
                "Refresh Token inválido."
            )

        user = await self.repository.get_by_id(
            UUID(payload.sub),
        )

        if user is None:
            raise UnauthorizedException(
                "Usuário não encontrado."
            )

        if not user.is_active:
            raise UnauthorizedException(
                "Usuário inativo."
            )

        return self._generate_tokens(user)

    async def get_user(
        self,
        user_id: UUID,
    ) -> User | None:

        return await self.repository.get_by_id(
            user_id,
        )