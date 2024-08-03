"""rev

Revision ID: 039bbc3604a3
Revises: e9193ccfc230
Create Date: 2024-08-03 05:06:46.515938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '039bbc3604a3'
down_revision: Union[str, None] = 'e9193ccfc230'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model', 'status',
               existing_type=mysql.INTEGER(),
               type_=sa.Boolean(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
