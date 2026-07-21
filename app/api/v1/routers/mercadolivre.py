from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.dependencies.auth import get_current_user
from app.dependencies.mercadolivre import (
    get_ml_oauth,
    get_ml_service,
)
from app.mappers.mercadolivre_mapper import MercadoLivreMapper
from app.models.user import User
from app.schemas.mercadolivre import (
    MercadoLivreConnectionResponse,
)
from app.services.ml_account_service import MLAccountService
from app.integrations.mercadolivre.oauth import MercadoLivreOAuth

router = APIRouter(
    prefix="/mercadolivre",
    tags=["Mercado Livre"],
)


@router.get(
    "/connect",
)
async def connect(
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
):
    """
    Retorna a URL de autorização OAuth.
    """

    return {
        "authorization_url": oauth.authorization_url(),
    }


@router.get(
    "/callback",
    response_model=MercadoLivreConnectionResponse,
)
async def callback(
    code: str = Query(...),
    current_user: User = Depends(get_current_user),
    oauth: MercadoLivreOAuth = Depends(get_ml_oauth),
    service: MLAccountService = Depends(get_ml_service),
):
    """
    Callback OAuth do Mercado Livre.
    """

    oauth_data = await oauth.exchange_code(code)

    profile = await oauth.get_current_user(
        oauth_data["access_token"],
    )

    create_schema = MercadoLivreMapper.to_create(
        profile=profile,
        oauth=oauth_data,
    )

    update_schema = MercadoLivreMapper.to_update(
        oauth=oauth_data,
    )

    await service.upsert(
        user_id=current_user.id,
        create_data=create_schema,
        update_data=update_schema,
    )

    return MercadoLivreConnectionResponse(
        success=True,
        message="Conta conectada com sucesso.",
        nickname=profile["nickname"],
        ml_user_id=profile["id"],
    )