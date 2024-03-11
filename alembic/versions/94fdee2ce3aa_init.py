"""Init

Revision ID: 94fdee2ce3aa
Revises: 9342a10f35b3
Create Date: 2024-03-11 19:49:11.289545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94fdee2ce3aa'
down_revision: Union[str, None] = '9342a10f35b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('user', sa.Column('created_on', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=False)
    op.alter_column('user', 'budget',
               existing_type=sa.BIGINT(),
               type_=sa.Float(),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.alter_column('user', 'name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=True)
    op.alter_column('user', 'budget',
               existing_type=sa.Float(),
               type_=sa.BIGINT(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=True)
    op.drop_column('user', 'active')
    op.drop_column('user', 'created_on')
    op.drop_column('user', 'id')
    # ### end Alembic commands ###