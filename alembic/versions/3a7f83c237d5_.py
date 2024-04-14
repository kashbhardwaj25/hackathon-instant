"""empty message

Revision ID: 3a7f83c237d5
Revises: e2be7a964f1c
Create Date: 2024-04-14 16:43:45.055233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a7f83c237d5'
down_revision: Union[str, None] = 'e2be7a964f1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_id_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_id_key', 'user', ['id'])
    # ### end Alembic commands ###
