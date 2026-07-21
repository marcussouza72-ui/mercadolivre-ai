from __future__ import annotations

from .common import MercadoLivreSchema


class UserResponse(MercadoLivreSchema):
    id: int
    nickname: str
    registration_date: str | None = None
    country_id: str
    site_id: str
    permalink: str | None = None