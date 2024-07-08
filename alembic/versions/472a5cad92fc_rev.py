"""rev

Revision ID: 472a5cad92fc
Revises: c0742a65f6e1
Create Date: 2024-07-08 18:06:23.971760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '472a5cad92fc'
down_revision: Union[str, None] = 'c0742a65f6e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hadith', 'hadith_arab',
               existing_type=mysql.CHAR(length=1),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('hadith', 'hadith_melayu',
               existing_type=mysql.CHAR(length=1),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.drop_column('hadith', 'hadith')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hadith', sa.Column('hadith', mysql.VARCHAR(length=255), nullable=True))
    op.alter_column('hadith', 'hadith_melayu',
               existing_type=sa.String(length=255),
               type_=mysql.CHAR(length=1),
               existing_nullable=True)
    op.alter_column('hadith', 'hadith_arab',
               existing_type=sa.String(length=255),
               type_=mysql.CHAR(length=1),
               existing_nullable=True)
    # ### end Alembic commands ###