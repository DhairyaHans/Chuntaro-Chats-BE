"""create users groups mapping table

Revision ID: 99b028d09e1d
Revises: c812bb2caa22
Create Date: 2026-03-19 00:41:15.243251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99b028d09e1d'
down_revision: Union[str, Sequence[str], None] = 'c812bb2caa22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "groups_users",
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("group_id", sa.UUID, nullable=False),
        sa.Column("is_admin", sa.Boolean, server_default="False"),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), nullable=False)
    )

    op.create_primary_key(
        "pkey_groups_users",
        "groups_users", 
        ["group_id", "user_id"]
    )

    op.create_index(
        "idx_groups_users_user_id_group_id",
        "groups_users",
        ["user_id", "group_id"]
    )
    
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "idx_groups_users_user_id_group_id",
        "groups_users"
    )
    op.drop_table("groups_users")
