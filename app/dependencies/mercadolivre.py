from __future__ import annotations

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.database.connection import get_db

from app.integrations.mercadolivre.api import MercadoLivreAPI
from app.integrations.mercadolivre.client import MercadoLivreClient
from app.integrations.mercadolivre.oauth import MercadoLivreOAuth
from app.integrations.mercadolivre.token_manager import TokenManager

from app.repositories.ml_account_repository import MLAccountRepository
from app.repositories.oauth_state_repository import OAuthStateRepository

from app.services.ml_account_service import MLAccountService
from app.services.oauth_state_service import OAuthStateService
from app.services.mercadolivre_oauth_service import MercadoLivreOAuthService


def get_ml_client() -> MercadoLivreClient:
    """
    Cliente HTTP utilizado pela integração Mercado Livre.
    """
    return MercadoLivreClient(
        base_url=settings.MELI_API_URL,
        timeout=settings.MELI_REQUEST_TIMEOUT,
    )


def get_ml_oauth(
    client: MercadoLivreClient = Depends(get_ml_client),
) -> MercadoLivreOAuth:
    """
    Serviço responsável pelas operações do protocolo OAuth.
    """
    return MercadoLivreOAuth(
        client=client,
    )


def get_ml_token_manager(
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
) -> TokenManager:
    """
    Responsável pelo cálculo de expiração e renovação de tokens.
    """
    return TokenManager(
        oauth=oauth,
    )


# ----------------------------------------------------------------------
# OAuth State
# ----------------------------------------------------------------------


def get_oauth_state_repository(
    db: AsyncSession = Depends(get_db),
) -> OAuthStateRepository:
    """
    Repositório responsável pelos OAuth States.
    """
    return OAuthStateRepository(
        session=db,
    )


def get_oauth_state_service(
    repository: OAuthStateRepository = Depends(
        get_oauth_state_repository,
    ),
) -> OAuthStateService:
    """
    Regras de negócio dos OAuth States.
    """
    return OAuthStateService(
        repository=repository,
    )


# ----------------------------------------------------------------------
# Mercado Livre Accounts
# ----------------------------------------------------------------------


def get_ml_repository(
    db: AsyncSession = Depends(get_db),
) -> MLAccountRepository:
    """
    Repositório das contas Mercado Livre.
    """
    return MLAccountRepository(
        session=db,
    )


def get_ml_service(
    repository: MLAccountRepository = Depends(
        get_ml_repository,
    ),
) -> MLAccountService:
    """
    Serviço responsável pelas regras de negócio
    das contas Mercado Livre.
    """
    return MLAccountService(
        repository=repository,
    )


# ----------------------------------------------------------------------
# OAuth Orchestrator
# ----------------------------------------------------------------------


def get_ml_oauth_service(
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
    token_manager: TokenManager = Depends(get_ml_token_manager),
    account_service: MLAccountService = Depends(get_ml_service),
) -> MercadoLivreOAuthService:
    """
    Orquestra todo o fluxo OAuth do Mercado Livre.
    """
    return MercadoLivreOAuthService(
        oauth=oauth,
        token_manager=token_manager,
        account_service=account_service,
    )


# ----------------------------------------------------------------------
# Mercado Livre API
# ----------------------------------------------------------------------


def get_ml_api(
    client: MercadoLivreClient = Depends(get_ml_client),
    token_manager: TokenManager = Depends(get_ml_token_manager),
    account_service: MLAccountService = Depends(get_ml_service),
) -> MercadoLivreAPI:
    """
    Fachada responsável pelas chamadas autenticadas
    à API do Mercado Livre.
    """
    return MercadoLivreAPI(
        client=client,
        token_manager=token_manager,
        account_service=account_service,
    )