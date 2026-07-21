from __future__ import annotations

from httpx import Response

from app.integrations.mercadolivre.client import MercadoLivreClient
from app.integrations.mercadolivre.token_manager import TokenManager
from app.models.ml_account import MLAccount
from app.schemas.ml_account import MLAccountUpdate
from app.services.ml_account_service import MLAccountService


class MercadoLivreAPI:
    """
    Fachada da API do Mercado Livre.

    Responsabilidades:

    - garantir que o access token esteja válido;
    - renovar automaticamente tokens expirados;
    - persistir os novos tokens;
    - executar chamadas autenticadas.
    """

    def __init__(
        self,
        *,
        client: MercadoLivreClient,
        token_manager: TokenManager,
        account_service: MLAccountService,
    ) -> None:
        self._client = client
        self._token_manager = token_manager
        self._account_service = account_service

    async def _get_access_token(
        self,
        account: MLAccount,
    ) -> str:
        """
        Retorna um access token válido.

        Caso o token esteja próximo da expiração,
        realiza automaticamente sua renovação.
        """

        oauth = await self._token_manager.ensure_valid_token(
            access_token=account.access_token,
            refresh_token=account.refresh_token,
            expires_at=account.expires_at,
        )

        if oauth is not None:

            account = await self._account_service.update_tokens(
                account=account,
                data=MLAccountUpdate(
                    access_token=oauth["access_token"],
                    refresh_token=oauth["refresh_token"],
                    token_type=oauth["token_type"],
                    scope=oauth.get("scope"),
                    expires_at=self._token_manager.expires_at(
                        oauth["expires_in"],
                    ),
                    is_active=True,
                ),
            )

        return account.access_token

    async def get(
        self,
        *,
        account: MLAccount,
        endpoint: str,
        params: dict | None = None,
    ) -> Response:
        """
        Executa uma requisição GET autenticada.
        """

        token = await self._get_access_token(account)

        return await self._client.get(
            endpoint=endpoint,
            params=params,
            access_token=token,
        )

    async def post(
        self,
        *,
        account: MLAccount,
        endpoint: str,
        json: dict | None = None,
    ) -> Response:
        """
        Executa uma requisição POST autenticada.
        """

        token = await self._get_access_token(account)

        return await self._client.post(
            endpoint=endpoint,
            json=json,
            access_token=token,
        )

    async def put(
        self,
        *,
        account: MLAccount,
        endpoint: str,
        json: dict | None = None,
    ) -> Response:
        """
        Executa uma requisição PUT autenticada.
        """

        token = await self._get_access_token(account)

        return await self._client.put(
            endpoint=endpoint,
            json=json,
            access_token=token,
        )

    async def delete(
        self,
        *,
        account: MLAccount,
        endpoint: str,
    ) -> Response:
        """
        Executa uma requisição DELETE autenticada.
        """

        token = await self._get_access_token(account)

        return await self._client.delete(
            endpoint=endpoint,
            access_token=token,
        )