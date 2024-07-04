"""rev

Revision ID: e50d759fae1f
Revises: 96c0b2ad0c29
Create Date: 2024-07-03 07:45:37.880174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e50d759fae1f'
down_revision: Union[str, None] = '96c0b2ad0c29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hadith_assesment', sa.Column('hadith_id', sa.Integer(), nullable=True))
    op.add_column('hadith_assesment', sa.Column('evaluation_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'hadith_assesment', 'type_hadith', ['evaluation_id'], ['id'])
    op.create_foreign_key(None, 'hadith_assesment', 'hadith', ['hadith_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hadith_assesment', type_='foreignkey')
    op.drop_constraint(None, 'hadith_assesment', type_='foreignkey')
    op.drop_column('hadith_assesment', 'evaluation_id')
    op.drop_column('hadith_assesment', 'hadith_id')
    # ### end Alembic commands ###