from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.ml_item import MLItem
    from app.models.user import User


class MLAccount(BaseModel):
    """
    Conta do Mercado Livre vinculada a um usuário do sistema.
    """

    __tablename__ = "ml_accounts"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    ml_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
        nullable=False,
    )

    nickname: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    site_id: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    access_token: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    refresh_token: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    token_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    scope: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="ml_accounts",
    )

    items: Mapped[list["MLItem"]] = relationship(
        "MLItem",
        back_populates="account",
        cascade="all, delete-orphan",
    )