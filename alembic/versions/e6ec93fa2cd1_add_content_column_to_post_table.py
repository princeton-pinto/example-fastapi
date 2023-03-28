"""add content column to post table

Revision ID: e6ec93fa2cd1
Revises: a079519a5664
Create Date: 2023-03-27 15:28:41.398921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6ec93fa2cd1'
down_revision = 'a079519a5664'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
