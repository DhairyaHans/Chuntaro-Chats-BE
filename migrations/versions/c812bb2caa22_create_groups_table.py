"""create groups table

Revision ID: c812bb2caa22
Revises: fc08aea3e14a
Create Date: 2025-12-24 01:20:51.497667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c812bb2caa22'
down_revision: Union[str, Sequence[str], None] = 'fc08aea3e14a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
