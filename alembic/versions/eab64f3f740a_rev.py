"""rev

Revision ID: eab64f3f740a
Revises: 70ed5d4c1f20
Create Date: 2024-06-25 19:31:35.341893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'eab64f3f740a'
down_revision: Union[str, None] = '70ed5d4c1f20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'role',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'role',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###
