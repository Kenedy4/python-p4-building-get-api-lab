"""add bakery and baked goods models

Revision ID: b8b32c894c1a
Revises: 1a660c242acb
Create Date: 2024-10-05 12:12:24.304582

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'b8b32c894c1a'
down_revision = '1a660c242acb'
branch_labels = None
depends_on = None

def upgrade():
    # 1. Add a new column with the correct type
    op.add_column('baked_goods', sa.Column('new_price', sa.Float(), nullable=True))

    # 2. Copy the data from the old column to the new column
    op.execute('UPDATE baked_goods SET new_price = price')

    # 3. Drop the old column (SQLite does not support direct drop, this step may need manual intervention)
    op.drop_column('baked_goods', 'price')

    # 4. Rename the new column to the old column's name
    op.alter_column('baked_goods', 'new_price', new_column_name='price')


def downgrade():
    # To reverse this, you'll need to re-add the old column type, copy data back, and drop the new column
    op.add_column('baked_goods', sa.Column('price', sa.Integer(), nullable=True))
    op.execute('UPDATE baked_goods SET price = new_price')
    op.drop_column('baked_goods', 'new_price')
