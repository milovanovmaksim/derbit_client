"""Added initial tables

Revision ID: 08b47eea72f0
Revises: 
Create Date: 2023-06-14 14:51:49.079493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08b47eea72f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickers',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=8), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idx')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickers')
    # ### end Alembic commands ###
