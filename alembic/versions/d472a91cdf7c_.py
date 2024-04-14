"""empty message

Revision ID: d472a91cdf7c
Revises: 3a7f83c237d5
Create Date: 2024-04-14 18:51:53.609923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd472a91cdf7c'
down_revision: Union[str, None] = '3a7f83c237d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('storedata', sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('storedata', 'user_id')
    # ### end Alembic commands ###