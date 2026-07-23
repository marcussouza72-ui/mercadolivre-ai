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

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session

    async def create(
        self,
        account: MLAccount,
    ) -> MLAccount:
        self._session.add(account)
        await self._session.commit()
        await self._session.refresh(account)
        return account

    async def update(
        self,
        account: MLAccount,
    ) -> MLAccount:
        await self._session.commit()
        await self._session.refresh(account)
        return account

    async def delete(
        self,
        account: MLAccount,
    ) -> None:
        await self._session.delete(account)
        await self._session.commit()

    async def get_by_id(
        self,
        account_id: UUID,
    ) -> MLAccount | None:
        return await self._session.get(
            MLAccount,
            account_id,
        )

    async def get_by_ml_user_id(
        self,
        ml_user_id: int,
    ) -> MLAccount | None:
        stmt = (
            select(MLAccount)
            .where(
                MLAccount.ml_user_id == ml_user_id,
            )
        )

        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def list_by_user(
        self,
        user_id: UUID,
    ) -> list[MLAccount]:
        stmt = (
            select(MLAccount)
            .where(
                MLAccount.user_id == user_id,
            )
            .order_by(
                MLAccount.created_at.desc(),
            )
        )

        result = await self._session.execute(stmt)

        return list(result.scalars().all())