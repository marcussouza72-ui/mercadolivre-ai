from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.ml_account import MLAccount
    from app.models.oauth_state import OAuthState


class User(BaseModel):
    """
    Usuário da aplicação.

    Um usuário pode conectar uma ou mais contas do Mercado Livre.
    """

    __tablename__ = "users"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
        nullable=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
    )

    ml_accounts: Mapped[list["MLAccount"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    oauth_states: Mapped[list["OAuthState"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )