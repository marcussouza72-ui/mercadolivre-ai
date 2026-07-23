"""change ml_user_id to bigint

Revision ID: dec0785003f1
Revises: 4a5d532dc7e1
Create Date: 2026-07-23 13:30:59.001895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dec0785003f1"
down_revision: Union[str, Sequence[str], None] = "4a5d532dc7e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "ml_accounts",
        "ml_user_id",
        existing_type=sa.Integer(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "ml_accounts",
        "ml_user_id",
        existing_type=sa.BigInteger(),
        type_=sa.Integer(),
        existing_nullable=False,
    )