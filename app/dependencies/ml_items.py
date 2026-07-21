from __future__ import annotations

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.integrations.mercadolivre.api import MercadoLivreAPI
from app.integrations.mercadolivre.items import MercadoLivreItems
from app.repositories.ml_item_repository import MLItemRepository
from app.services.ml_item_service import MLItemService


def get_ml_item_repository(
    db: AsyncSession = Depends(get_db),
) -> MLItemRepository:
    """
    Dependency que fornece o repositório de anúncios.
    """
    return MLItemRepository(db)


def get_ml_item_service(
    repository: MLItemRepository = Depends(get_ml_item_repository),
) -> MLItemService:
    """
    Dependency que fornece o serviço de anúncios.
    """
    return MLItemService(repository)


def get_mercadolivre_items(
    api: MercadoLivreAPI = Depends(),
) -> MercadoLivreItems:
    """
    Dependency que fornece o cliente da API de anúncios.
    """
    return MercadoLivreItems(api)