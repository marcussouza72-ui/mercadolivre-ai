from __future__ import annotations

from uuid import UUID

from app.models.ml_item import MLItem
from app.repositories.ml_item_repository import MLItemRepository


class MLItemService:
    """
    Camada de negócio responsável pelos anúncios armazenados
    localmente no banco de dados.
    """

    def __init__(
        self,
        repository: MLItemRepository,
    ) -> None:
        self._repository = repository

    async def get(
        self,
        item_id: UUID,
    ) -> MLItem | None:
        """
        Obtém um anúncio pelo ID interno.
        """
        return await self._repository.get_by_id(item_id)

    async def find_by_ml_item_id(
        self,
        ml_item_id: str,
    ) -> MLItem | None:
        """
        Obtém um anúncio pelo ID do Mercado Livre.
        """
        return await self._repository.get_by_ml_item_id(
            ml_item_id
        )

    async def list_account_items(
        self,
        account_id: UUID,
    ) -> list[MLItem]:
        """
        Lista todos os anúncios de uma conta.
        """
        return await self._repository.list_by_account(
            account_id
        )

    async def create(
        self,
        item: MLItem,
    ) -> MLItem:
        """
        Cria um novo anúncio.
        """
        return await self._repository.create(item)

    async def update(
        self,
        item: MLItem,
    ) -> MLItem:
        """
        Atualiza um anúncio existente.
        """
        return await self._repository.update(item)

    async def delete(
        self,
        item: MLItem,
    ) -> None:
        """
        Remove um anúncio.
        """
        await self._repository.delete(item)

    async def upsert(
        self,
        item: MLItem,
    ) -> MLItem:
        """
        Cria ou atualiza um anúncio.
        """
        existing = await self.find_by_ml_item_id(
            item.ml_item_id
        )

        if existing is None:
            return await self.create(item)

        existing.title = item.title
        existing.category_id = item.category_id
        existing.listing_type_id = item.listing_type_id
        existing.condition = item.condition
        existing.status = item.status
        existing.permalink = item.permalink
        existing.price = item.price
        existing.currency_id = item.currency_id
        existing.available_quantity = item.available_quantity
        existing.sold_quantity = item.sold_quantity
        existing.accepts_mercadopago = item.accepts_mercadopago
        existing.catalog_listing = item.catalog_listing

        return await self.update(existing)