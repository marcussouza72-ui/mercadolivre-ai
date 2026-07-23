from __future__ import annotations

import secrets
from datetime import UTC, datetime, timedelta
from uuid import UUID

from app.core.exceptions import InvalidOAuthStateError
from app.models.oauth_state import OAuthState
from app.repositories.oauth_state_repository import (
    OAuthStateRepository,
)


class OAuthStateService:
    """
    Camada de regras de negócio responsável pelos states
    utilizados durante o fluxo OAuth.

    Responsabilidades:

    - gerar states seguros;
    - controlar expiração;
    - validar states;
    - impedir reutilização;
    - limpar registros expirados.
    """

    STATE_EXPIRATION_MINUTES = 10

    def __init__(
        self,
        repository: OAuthStateRepository,
    ) -> None:
        self._repository = repository

    async def create_state(
        self,
        *,
        user_id: UUID,
    ) -> OAuthState:
        """
        Gera um novo state para o usuário.
        """

        oauth_state = OAuthState(
            state=secrets.token_urlsafe(32),
            user_id=user_id,
            expires_at=datetime.now(UTC)
            + timedelta(minutes=self.STATE_EXPIRATION_MINUTES),
            used=False,
        )

        return await self._repository.create(oauth_state)

    async def consume_state(
        self,
        *,
        state: str,
    ) -> OAuthState:
        """
        Valida um state e o marca como utilizado.
        """

        oauth_state = await self._repository.get_valid_state(
            state,
        )

        if oauth_state is None:
            raise InvalidOAuthStateError(
                "OAuth state inválido ou expirado."
            )

        return await self._repository.mark_used(
            oauth_state,
        )

    async def cleanup_expired(
        self,
    ) -> int:
        """
        Remove states expirados.
        """

        return await self._repository.delete_expired()