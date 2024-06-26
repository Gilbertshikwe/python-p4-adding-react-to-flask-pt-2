"""Add release_date, runtime, director, and cast columns to Movie model

Revision ID: ecb7cc1ca36d
Revises: ad6df61696c5
Create Date: 2024-04-12 18:02:47.222350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecb7cc1ca36d'
down_revision = 'ad6df61696c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('release_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('runtime', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('director', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('cast', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.drop_column('cast')
        batch_op.drop_column('director')
        batch_op.drop_column('runtime')
        batch_op.drop_column('release_date')

    # ### end Alembic commands ###
