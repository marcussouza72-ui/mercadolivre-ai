from __future__ import annotations

from httpx import Response

from app.integrations.mercadolivre.api import MercadoLivreAPI
from app.integrations.mercadolivre.endpoints import ENDPOINTS
from app.models.ml_account import MLAccount


class MercadoLivreUsers:
    """
    Endpoints relacionados aos usuários do Mercado Livre.

    Esta classe encapsula exclusivamente operações do recurso
    Users da API.
    """

    def __init__(
        self,
        api: MercadoLivreAPI,
    ) -> None:
        self._api = api

    async def get_me(
        self,
        account: MLAccount,
    ) -> Response:
        """
        Retorna os dados do usuário autenticado.
        """

        return await self._api.get(
            account=account,
            endpoint=ENDPOINTS.USER_ME,
        )

    async def get_user(
        self,
        *,
        account: MLAccount,
        user_id: int,
    ) -> Response:
        """
        Consulta um usuário pelo ID.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/users/{user_id}",
        )

    async def get_reputation(
        self,
        *,
        account: MLAccount,
        user_id: int,
    ) -> Response:
        """
        Obtém a reputação de um usuário.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/users/{user_id}/reputation",
        )

    async def get_addresses(
        self,
        *,
        account: MLAccount,
        user_id: int,
    ) -> Response:
        """
        Lista os endereços cadastrados pelo usuário.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/users/{user_id}/addresses",
        )

    async def get_brands(
        self,
        *,
        account: MLAccount,
        user_id: int,
    ) -> Response:
        """
        Lista as marcas pertencentes ao usuário.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/users/{user_id}/brands",
        )