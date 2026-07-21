from __future__ import annotations

from .common import MercadoLivreSchema


class OAuthTokenResponse(MercadoLivreSchema):
    access_token: str
    token_type: str
    expires_in: int
    scope: str | None = None
    user_id: int
    refresh_token: str