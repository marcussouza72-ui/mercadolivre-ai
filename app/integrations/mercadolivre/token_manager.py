from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

from app.integrations.mercadolivre.oauth import MercadoLivreOAuth


class TokenManager:
    """
    Gerencia o ciclo de vida dos tokens OAuth do Mercado Livre.

    Responsabilidades:

    - calcular a expiração do token;
    - verificar se o token expirou;
    - verificar se o token está próximo da expiração;
    - renovar access tokens utilizando refresh tokens.
    """

    def __init__(
        self,
        oauth: MercadoLivreOAuth,
    ) -> None:
        self._oauth = oauth

    @staticmethod
    def expires_at(
        expires_in: int,
    ) -> datetime:
        """
        Calcula a data/hora de expiração do access token.
        """

        return datetime.now(UTC) + timedelta(seconds=expires_in)

    @staticmethod
    def is_expired(
        expires_at: datetime,
    ) -> bool:
        """
        Retorna True caso o token já esteja expirado.
        """

        return datetime.now(UTC) >= expires_at

    @staticmethod
    def expires_soon(
        expires_at: datetime,
        *,
        seconds: int = 300,
    ) -> bool:
        """
        Verifica se o token expirará em breve.

        Por padrão considera 5 minutos.
        """

        return datetime.now(UTC) >= (
            expires_at - timedelta(seconds=seconds)
        )

    async def refresh(
        self,
        refresh_token: str,
    ) -> dict[str, Any]:
        """
        Solicita um novo access token utilizando
        um refresh token válido.
        """

        return await self._oauth.refresh_token(
            refresh_token,
        )

    async def ensure_valid_token(
        self,
        *,
        access_token: str,
        refresh_token: str,
        expires_at: datetime,
    ) -> dict[str, Any] | None:
        """
        Garante que o token ainda seja válido.

        Retorna:

        - None → token continua válido.
        - dict → resposta da renovação do OAuth.
        """

        if self.expires_soon(expires_at):
            return await self.refresh(refresh_token)

        return None