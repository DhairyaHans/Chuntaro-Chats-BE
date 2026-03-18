"""add foreign key to groups

Revision ID: 57b3f0557fa5
Revises: 99b028d09e1d
Create Date: 2026-03-19 02:56:12.919005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57b3f0557fa5'
down_revision: Union[str, Sequence[str], None] = '99b028d09e1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_foreign_key(
        "fk_groups_owner",
        "groups",
        "users",
        ["owner_id"],
        ["id"]
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_groups_owner", "groups", type_="foreignkey")
