from __future__ import annotations

from datetime import datetime
from uuid import UUID

from app.integrations.mercadolivre.oauth import MercadoLivreOAuth
from app.integrations.mercadolivre.token_manager import TokenManager
from app.models.ml_account import MLAccount
from app.schemas.ml_account import (
    MLAccountCreate,
    MLAccountUpdate,
)
from app.services.ml_account_service import MLAccountService


class MercadoLivreOAuthService:
    """
    Orquestra todo o fluxo OAuth do Mercado Livre.

    Responsabilidades:

    - trocar authorization_code por access_token;
    - obter os dados da conta (/users/me);
    - calcular expires_at;
    - criar os schemas de persistência;
    - delegar a persistência ao MLAccountService.

    Não realiza acesso direto ao banco de dados.
    """

    def __init__(
        self,
        oauth: MercadoLivreOAuth,
        token_manager: TokenManager,
        account_service: MLAccountService,
    ) -> None:
        self._oauth = oauth
        self._token_manager = token_manager
        self._account_service = account_service

    async def connect_account(
        self,
        *,
        user_id: UUID,
        code: str,
    ) -> MLAccount:
        """
        Conecta uma conta Mercado Livre ao usuário da aplicação.
        """

        #
        # 1 - troca o authorization_code pelo token
        #
        token = await self._oauth.exchange_code(code)

        #
        # 2 - obtém os dados da conta Mercado Livre
        #
        ml_user = await self._oauth.get_current_user(
            token["access_token"],
        )

        #
        # 3 - calcula a data de expiração
        #
        expires_at: datetime = self._token_manager.expires_at(
            token["expires_in"],
        )

        #
        # 4 - schema de criação
        #
        create_data = MLAccountCreate(
            ml_user_id=ml_user["id"],
            nickname=ml_user["nickname"],
            site_id=ml_user["site_id"],
            access_token=token["access_token"],
            refresh_token=token["refresh_token"],
            token_type=token["token_type"],
            scope=token.get("scope"),
            expires_at=expires_at,
            is_active=True,
        )

        #
        # 5 - schema de atualização
        #
        update_data = MLAccountUpdate(
            access_token=token["access_token"],
            refresh_token=token["refresh_token"],
            token_type=token["token_type"],
            scope=token.get("scope"),
            expires_at=expires_at,
            is_active=True,
        )

        #
        # 6 - persiste a conta
        #
        account = await self._account_service.upsert(
            user_id=user_id,
            create_data=create_data,
            update_data=update_data,
        )

        return account