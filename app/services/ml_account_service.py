from __future__ import annotations

from uuid import UUID

from app.models.ml_account import MLAccount
from app.repositories.ml_account_repository import MLAccountRepository
from app.schemas.ml_account import (
    MLAccountCreate,
    MLAccountUpdate,
)


class MLAccountService:
    """
    Camada de regras de negócio das contas Mercado Livre.

    Responsabilidades:

    - criar contas;
    - localizar contas;
    - atualizar tokens;
    - ativar/desativar contas;
    - remover contas;
    - realizar upsert.
    """

    def __init__(
        self,
        repository: MLAccountRepository,
    ) -> None:
        self._repository = repository

    async def create(
        self,
        *,
        user_id: UUID,
        data: MLAccountCreate,
    ) -> MLAccount:
        """
        Cria uma nova conta Mercado Livre.
        """

        account = MLAccount(
            user_id=user_id,
            ml_user_id=data.ml_user_id,
            nickname=data.nickname,
            site_id=data.site_id,
            access_token=data.access_token,
            refresh_token=data.refresh_token,
            token_type=data.token_type,
            scope=data.scope,
            expires_at=data.expires_at,
            is_active=data.is_active,
        )

        return await self._repository.create(account)

    async def get_by_id(
        self,
        account_id: UUID,
    ) -> MLAccount | None:
        """
        Localiza uma conta pelo ID.
        """
        return await self._repository.get_by_id(account_id)

    async def get_by_ml_user_id(
        self,
        ml_user_id: int,
    ) -> MLAccount | None:
        """
        Localiza uma conta pelo usuário Mercado Livre.
        """
        return await self._repository.get_by_ml_user_id(
            ml_user_id,
        )

    async def list_user_accounts(
        self,
        user_id: UUID,
    ) -> list[MLAccount]:
        """
        Lista todas as contas Mercado Livre de um usuário.
        """
        return await self._repository.list_by_user(user_id)

    async def update_tokens(
        self,
        *,
        account: MLAccount,
        data: MLAccountUpdate,
    ) -> MLAccount:
        """
        Atualiza exclusivamente os dados OAuth.
        """

        if data.access_token is not None:
            account.access_token = data.access_token

        if data.refresh_token is not None:
            account.refresh_token = data.refresh_token

        if data.token_type is not None:
            account.token_type = data.token_type

        if data.scope is not None:
            account.scope = data.scope

        if data.expires_at is not None:
            account.expires_at = data.expires_at

        if data.is_active is not None:
            account.is_active = data.is_active
        else:
            account.is_active = True

        return await self._repository.update(account)

    async def activate(
        self,
        account: MLAccount,
    ) -> MLAccount:
        """
        Ativa uma conta.
        """

        account.is_active = True

        return await self._repository.update(account)

    async def deactivate(
        self,
        account: MLAccount,
    ) -> MLAccount:
        """
        Desativa uma conta.
        """

        account.is_active = False

        return await self._repository.update(account)

    async def delete(
        self,
        account: MLAccount,
    ) -> None:
        """
        Remove uma conta.
        """

        await self._repository.delete(account)

    async def upsert(
        self,
        *,
        user_id: UUID,
        create_data: MLAccountCreate,
        update_data: MLAccountUpdate,
    ) -> MLAccount:
        """
        Cria uma conta caso ela não exista ou atualiza seus
        tokens caso já exista.
        """

        account = await self.get_by_ml_user_id(
            create_data.ml_user_id,
        )

        if account is None:
            return await self.create(
                user_id=user_id,
                data=create_data,
            )

        return await self.update_tokens(
            account=account,
            data=update_data,
        )