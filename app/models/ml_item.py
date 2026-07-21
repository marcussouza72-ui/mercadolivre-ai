from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class MLItem(BaseModel):
    """
    Espelho local de um anúncio do Mercado Livre.
    """

    __tablename__ = "ml_items"

    account_id: Mapped[UUID] = mapped_column(
        ForeignKey("ml_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    ml_item_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
    )

    category_id: Mapped[str | None] = mapped_column(
        String(50),
    )

    listing_type_id: Mapped[str | None] = mapped_column(
        String(50),
    )

    condition: Mapped[str | None] = mapped_column(
        String(30),
    )

    status: Mapped[str | None] = mapped_column(
        String(30),
    )

    permalink: Mapped[str | None] = mapped_column(
        Text,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
    )

    currency_id: Mapped[str] = mapped_column(
        String(10),
    )

    available_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    sold_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    accepts_mercadopago: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    catalog_listing: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    account = relationship(
        "MLAccount",
        back_populates="items",
    )