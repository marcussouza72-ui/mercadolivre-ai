from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Classe base do SQLAlchemy.

    Todos os modelos da aplicação herdam, indiretamente,
    desta classe.
    """

    pass


class BaseModel(Base):
    """
    Classe base abstrata para todos os modelos.

    Fornece automaticamente:

    - id (UUID)
    - created_at
    - updated_at
    """

    __abstract__ = True

    __mapper_args__ = {
        "eager_defaults": True,
    }

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )