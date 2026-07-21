from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MLAccountBase(BaseModel):
    """
    Campos públicos de uma conta do Mercado Livre.
    """

    ml_user_id: int
    nickname: str
    site_id: str
    is_active: bool


class MLAccountCreate(MLAccountBase):
    """
    Dados necessários para criar uma conta do Mercado Livre.
    """

    access_token: str
    refresh_token: str
    token_type: str
    scope: str
    expires_at: datetime


class MLAccountUpdate(BaseModel):
    """
    Campos atualizáveis.
    """

    access_token: str | None = None
    refresh_token: str | None = None
    token_type: str | None = None
    scope: str | None = None
    expires_at: datetime | None = None
    is_active: bool | None = None


class MLAccountRead(MLAccountBase):
    """
    Representação pública de uma conta vinculada.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime