"""create posts tables

Revision ID: a079519a5664
Revises: 
Create Date: 2023-03-27 15:17:04.182031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a079519a5664'
down_revision = None
branch_labels = None
depends_on = None

# https://alembic.sqlalchemy.org/en/latest/api/ddl.html

def upgrade() -> None:
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop('posts')
    pass
