"""change scope to text

Revision ID: 147117707c58
Revises: dec0785003f1
Create Date: 2026-07-23 15:34:49.684982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "147117707c58"
down_revision: Union[str, Sequence[str], None] = "dec0785003f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "ml_accounts",
        "scope",
        existing_type=sa.String(length=255),
        type_=sa.Text(),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "ml_accounts",
        "scope",
        existing_type=sa.Text(),
        type_=sa.String(length=255),
        existing_nullable=False,
    )