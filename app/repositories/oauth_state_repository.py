from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.oauth_state import OAuthState


class OAuthStateRepository:
    """
    Repositório responsável pelo gerenciamento dos states
    utilizados durante o fluxo OAuth do Mercado Livre.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def _commit_refresh(
        self,
        entity: OAuthState,
    ) -> OAuthState:
        await self._session.commit()
        await self._session.refresh(entity)
        return entity

    async def create(
        self,
        oauth_state: OAuthState,
    ) -> OAuthState:
        self._session.add(oauth_state)
        return await self._commit_refresh(oauth_state)

    async def get_valid_state(
        self,
        state: str,
    ) -> OAuthState | None:
        stmt = (
            select(OAuthState)
            .where(OAuthState.state == state)
            .where(OAuthState.used.is_(False))
            .where(OAuthState.expires_at > datetime.now(UTC))
        )

        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def mark_used(
        self,
        oauth_state: OAuthState,
    ) -> OAuthState:
        oauth_state.used = True
        return await self._commit_refresh(oauth_state)

    async def delete_expired(self) -> int:
        stmt = delete(OAuthState).where(
            OAuthState.expires_at < datetime.now(UTC)
        )

        result = await self._session.execute(stmt)

        await self._session.commit()

        return result.rowcount or 0