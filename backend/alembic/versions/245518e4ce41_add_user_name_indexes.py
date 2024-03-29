"""add user name indexes

Revision ID: 245518e4ce41
Revises: 36d11b3df023
Create Date: 2023-05-12 16:16:14.052578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '245518e4ce41'
down_revision = '36d11b3df023'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    op.create_index(op.f('users_name_trgm_idx'), 'users', ['name'], postgresql_using='gin',
                    postgresql_ops={
                        'name': 'gin_trgm_ops',
                    }, unique=False)
    op.create_index(op.f('users_name_text_pattern_ops_idx'), 'users', ['name'],
                    postgresql_ops={
                        'name': 'text_pattern_ops',
                    })
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('users_name_trgm_idx'), table_name='users')
    op.drop_index(op.f('users_name_text_pattern_ops_idx'), table_name='users')
    # ### end Alembic commands ###
