from __future__ import annotations

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from app.dependencies.auth import get_current_user
from app.dependencies.mercadolivre import (
    get_ml_oauth,
    get_ml_oauth_service,
)
from app.integrations.mercadolivre.oauth import MercadoLivreOAuth
from app.models.user import User
from app.schemas.ml_account import MLAccountRead
from app.services.mercadolivre_oauth_service import MercadoLivreOAuthService

router = APIRouter(
    prefix="/mercadolivre",
    tags=["Mercado Livre"],
)


@router.get(
    "/connect",
    summary="Conectar conta Mercado Livre",
)
async def connect(
    current_user: User = Depends(get_current_user),
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
):
    """
    Redireciona o usuário para a tela de autorização
    do Mercado Livre.
    """

    authorization_url = oauth.authorization_url(
        state=str(current_user.id),
    )

    return RedirectResponse(
        url=authorization_url,
    )


@router.get(
    "/callback",
    response_model=MLAccountRead,
    summary="Callback OAuth Mercado Livre",
)
async def callback(
    code: str,
    state: str,
    oauth_service: MercadoLivreOAuthService = Depends(
        get_ml_oauth_service,
    ),
):
    """
    Recebe o callback do Mercado Livre após a autorização
    da conta.

    Toda a lógica do fluxo OAuth é delegada ao
    MercadoLivreOAuthService.
    """

    account = await oauth_service.connect_account(
        user_id=state,
        code=code,
    )

    return MLAccountRead.model_validate(account)