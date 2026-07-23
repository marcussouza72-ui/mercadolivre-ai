from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.user import User


class OAuthState(BaseModel):
    """
    Armazena os estados temporários utilizados durante o
    fluxo OAuth do Mercado Livre.

    Cada registro representa uma tentativa de autenticação
    iniciada por um usuário da plataforma.
    """

    __tablename__ = "oauth_states"

    state: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        index=True,
        nullable=False,
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    used: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="oauth_states",
    )