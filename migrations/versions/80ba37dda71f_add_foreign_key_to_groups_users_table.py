"""add foreign key to groups_users table

Revision ID: 80ba37dda71f
Revises: 57b3f0557fa5
Create Date: 2026-03-19 04:01:08.330362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80ba37dda71f'
down_revision: Union[str, Sequence[str], None] = '57b3f0557fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_foreign_key(
        "fk_groups_users_user_id",
        "groups_users",
        "users",
        ["user_id"],
        ["id"]
    )

    op.create_foreign_key(
        "fk_groups_users_group_id",
        "groups_users",
        "groups",
        ["group_id"],
        ["uuid"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_groups_users_user_id", "groups_users", type_="foreignkey")
    op.drop_constraint("fk_groups_users_group_id", "groups_users", type_="foreignkey")
