"""empty message

Revision ID: 0d649c53e176
Revises: d472a91cdf7c
Create Date: 2024-04-14 22:48:44.160599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d649c53e176'
down_revision: Union[str, None] = 'd472a91cdf7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('storedata_id_key', 'storedata', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('storedata_id_key', 'storedata', ['id'])
    # ### end Alembic commands ###