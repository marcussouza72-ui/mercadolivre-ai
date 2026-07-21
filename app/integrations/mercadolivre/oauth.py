from __future__ import annotations

from urllib.parse import urlencode

from app.core.config import settings
from app.integrations.mercadolivre.client import MercadoLivreClient
from app.integrations.mercadolivre.endpoints import (
    AUTH_BASE_URL,
    OAUTH_AUTHORIZE,
    OAUTH_TOKEN,
    USERS_ME,
)


class MercadoLivreOAuth:
    """
    Responsável por encapsular o fluxo OAuth 2.0 do Mercado Livre.

    Esta classe NÃO possui regras de negócio e NÃO realiza
    persistência de dados. Sua única responsabilidade é executar
    as operações do protocolo OAuth utilizando o MercadoLivreClient.
    """

    def __init__(
        self,
        client: MercadoLivreClient,
    ) -> None:
        self._client = client

    def authorization_url(
        self,
        state: str | None = None,
    ) -> str:
        """
        Gera a URL de autorização do Mercado Livre.
        """

        params = {
            "response_type": "code",
            "client_id": settings.MELI_CLIENT_ID,
            "redirect_uri": settings.MELI_REDIRECT_URI,
        }

        if state:
            params["state"] = state

        return (
            f"{AUTH_BASE_URL}"
            f"{OAUTH_AUTHORIZE}"
            f"?{urlencode(params)}"
        )

    async def exchange_code(
        self,
        code: str,
    ) -> dict:
        """
        Troca o authorization_code por access_token.
        """

        payload = {
            "grant_type": "authorization_code",
            "client_id": settings.MELI_CLIENT_ID,
            "client_secret": settings.MELI_CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.MELI_REDIRECT_URI,
        }

        response = await self._client.post(
            OAUTH_TOKEN,
            data=payload,
        )

        response.raise_for_status()

        return response.json()

    async def refresh_token(
        self,
        refresh_token: str,
    ) -> dict:
        """
        Solicita um novo access_token utilizando
        um refresh_token válido.
        """

        payload = {
            "grant_type": "refresh_token",
            "client_id": settings.MELI_CLIENT_ID,
            "client_secret": settings.MELI_CLIENT_SECRET,
            "refresh_token": refresh_token,
        }

        response = await self._client.post(
            OAUTH_TOKEN,
            data=payload,
        )

        response.raise_for_status()

        return response.json()

    async def get_current_user(
        self,
        access_token: str,
    ) -> dict:
        """
        Recupera as informações da conta autenticada
        (/users/me).
        """

        response = await self._client.get(
            USERS_ME,
            access_token=access_token,
        )

        response.raise_for_status()

        return response.json()