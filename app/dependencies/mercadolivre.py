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
from app.services.ml_account_service import MLAccountService
from app.services.mercadolivre_oauth_service import MercadoLivreOAuthService

def get_ml_client() -> MercadoLivreClient:
    return MercadoLivreClient(
        base_url=settings.MELI_API_URL,
        timeout=settings.MELI_REQUEST_TIMEOUT,
    )

def get_ml_oauth(
    client: MercadoLivreClient = Depends(get_ml_client),
) -> MercadoLivreOAuth:
    """
    Serviço responsável pelo fluxo OAuth do Mercado Livre.
    """
    return MercadoLivreOAuth(
        client=client,
    )

def get_ml_token_manager(
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
) -> TokenManager:
    """
    Gerenciador responsável por validar e renovar tokens.
    """
    return TokenManager(
        oauth=oauth,
    )

def get_ml_repository(
    db: AsyncSession = Depends(get_db),
) -> MLAccountRepository:
    """
    Fornece o repositório das contas Mercado Livre.
    """
    return MLAccountRepository(db)

def get_ml_service(
    repository: MLAccountRepository = Depends(get_ml_repository),
) -> MLAccountService:
    """
    Fornece o serviço responsável pelas regras de negócio
    das contas Mercado Livre.
    """
    return MLAccountService(
        repository=repository,
    )

def get_ml_api(
    client: MercadoLivreClient = Depends(get_ml_client),
    token_manager: TokenManager = Depends(get_ml_token_manager),
    account_service: MLAccountService = Depends(get_ml_service),
) -> MercadoLivreAPI:
    """
    Fachada da API do Mercado Livre.

    Responsável por:

    - validar tokens;
    - renovar tokens expirados;
    - persistir novos tokens;
    - executar chamadas autenticadas.
    """
    return MercadoLivreAPI(
        client=client,
        token_manager=token_manager,
        account_service=account_service,
    )

def get_ml_oauth_service(
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
    token_manager: TokenManager = Depends(get_ml_token_manager),
    account_service: MLAccountService = Depends(get_ml_service),
) -> MercadoLivreOAuthService:
    """
    Serviço responsável por orquestrar todo o fluxo OAuth
    do Mercado Livre.
    """
    return MercadoLivreOAuthService(
        oauth=oauth,
        token_manager=token_manager,
        account_service=account_service,
    )