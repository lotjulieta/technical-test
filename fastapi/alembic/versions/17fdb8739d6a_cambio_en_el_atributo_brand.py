"""Cambio en el atributo 'brand'

Revision ID: 17fdb8739d6a
Revises: f0d35e92a42b
Create Date: 2024-07-02 18:25:28.921329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17fdb8739d6a'
down_revision: Union[str, None] = 'f0d35e92a42b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('brand', sa.String(), nullable=False))
    op.drop_column('cars', 'content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('cars', 'brand')
    # ### end Alembic commands ###
