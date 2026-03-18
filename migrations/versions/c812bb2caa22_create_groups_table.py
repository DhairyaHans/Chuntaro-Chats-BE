"""create groups table

Revision ID: c812bb2caa22
Revises: fc08aea3e14a
Create Date: 2025-12-24 01:20:51.497667

"""
from typing import Sequence, Union

from sqlalchemy import text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c812bb2caa22'
down_revision: Union[str, Sequence[str], None] = 'fc08aea3e14a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "groups",
        sa.Column("uuid", sa.UUID, primary_key=True, server_default=text("gen_random_uuid()")),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String),
        sa.Column("owner_id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime,server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime,server_default=sa.func.now(), nullable=False),
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("groups")
