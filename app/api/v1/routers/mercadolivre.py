from __future__ import annotations

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)

from app.core.exceptions import (
    InvalidOAuthStateError,
    MLAccountAlreadyLinkedError,
)
from app.dependencies.auth import get_current_user
from app.dependencies.mercadolivre import (
    get_ml_oauth_service,
    get_oauth_state_service,
)
from app.models.user import User
from app.schemas.mercadolivre import (
    MercadoLivreAuthorizationResponse,
    MercadoLivreConnectionResponse,
)
from app.services.mercadolivre_oauth_service import (
    MercadoLivreOAuthService,
)
from app.services.oauth_state_service import (
    OAuthStateService,
)

router = APIRouter(
    prefix="/mercadolivre",
    tags=["Mercado Livre"],
)


@router.get(
    "/connect",
    response_model=MercadoLivreAuthorizationResponse,
)
async def connect(
    current_user: User = Depends(get_current_user),
    oauth_service: MercadoLivreOAuthService = Depends(
        get_ml_oauth_service,
    ),
    oauth_state_service: OAuthStateService = Depends(
        get_oauth_state_service,
    ),
) -> MercadoLivreAuthorizationResponse:
    """
    Inicia o fluxo OAuth do Mercado Livre.

    Gera um OAuth State associado ao usuário autenticado
    e retorna a URL de autorização.
    """

    oauth_state = await oauth_state_service.create_state(
        user_id=current_user.id,
    )

    authorization_url = oauth_service.build_authorization_url(
        state=oauth_state.state,
    )

    return MercadoLivreAuthorizationResponse(
        authorization_url=authorization_url,
    )


@router.get(
    "/callback",
    response_model=MercadoLivreConnectionResponse,
)
async def callback(
    code: str = Query(
        ...,
        description="Authorization Code retornado pelo Mercado Livre.",
    ),
    state: str = Query(
        ...,
        description="OAuth State retornado pelo Mercado Livre.",
    ),
    oauth_service: MercadoLivreOAuthService = Depends(
        get_ml_oauth_service,
    ),
    oauth_state_service: OAuthStateService = Depends(
        get_oauth_state_service,
    ),
) -> MercadoLivreConnectionResponse:
    """
    Callback OAuth do Mercado Livre.

    Fluxo:

    1. Valida o OAuth State.
    2. Marca o State como utilizado.
    3. Troca o Authorization Code por Access Token.
    4. Obtém os dados da conta Mercado Livre.
    5. Cria ou atualiza a conta vinculada ao usuário.
    """

    try:
        oauth_state = await oauth_state_service.consume_state(
            state=state,
        )
    except InvalidOAuthStateError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    try:
        account = await oauth_service.connect_account(
            user_id=oauth_state.user_id,
            code=code,
        )
    except MLAccountAlreadyLinkedError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    return MercadoLivreConnectionResponse(
        success=True,
        message="Conta Mercado Livre conectada com sucesso.",
        nickname=account.nickname,
        ml_user_id=account.ml_user_id,
    )