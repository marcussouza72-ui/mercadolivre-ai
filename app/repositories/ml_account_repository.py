from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ml_account import MLAccount


class MLAccountRepository:
    """
    Repositório responsável pelo acesso aos dados das contas
    do Mercado Livre.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session