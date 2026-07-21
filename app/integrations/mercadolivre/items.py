from __future__ import annotations

from httpx import Response

from app.integrations.mercadolivre.api import MercadoLivreAPI
from app.integrations.mercadolivre.endpoints import ENDPOINTS
from app.models.ml_account import MLAccount


class MercadoLivreItems:
    """
    Cliente responsável pelos endpoints relacionados
    aos anúncios (Items) do Mercado Livre.
    """

    def __init__(
        self,
        api: MercadoLivreAPI,
    ) -> None:
        self._api = api

    async def search_items(
        self,
        *,
        account: MLAccount,
        user_id: int,
        limit: int = 50,
        offset: int = 0,
    ) -> Response:
        """
        Lista os IDs dos anúncios do vendedor.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/users/{user_id}/items/search",
            params={
                "limit": limit,
                "offset": offset,
            },
        )

    async def get_item(
        self,
        *,
        account: MLAccount,
        item_id: str,
    ) -> Response:
        """
        Obtém os detalhes completos de um anúncio.
        """

        return await self._api.get(
            account=account,
            endpoint=f"/items/{item_id}",
        )

    async def get_multiple_items(
        self,
        *,
        account: MLAccount,
        item_ids: list[str],
    ) -> Response:
        """
        Consulta diversos anúncios em uma única chamada.
        """

        ids = ",".join(item_ids)

        return await self._api.get(
            account=account,
            endpoint="/items",
            params={
                "ids": ids,
            },
        )