"""add message text indexes

Revision ID: 932ed12fed02
Revises: 245518e4ce41
Create Date: 2023-05-12 16:34:05.211816

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '932ed12fed02'
down_revision = '245518e4ce41'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    op.create_index(op.f('messages_text_trgm_idx'), 'messages', ['text'], postgresql_using='gin',
                    postgresql_ops={
                        'text': 'gin_trgm_ops',
                    }, unique=False)
    op.create_index(op.f('messages_text_ts_idx'), 'messages', [sa.text("to_tsvector('russian', text)")],
                    postgresql_using='gin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('messages_text_trgm_idx'), table_name='messages')
    op.drop_index(op.f('messages_text_ts_idx'), table_name='messages')
    # ### end Alembic commands ###
