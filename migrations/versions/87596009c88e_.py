"""empty message

Revision ID: 87596009c88e
Revises: aed2d873ca8c
Create Date: 2024-04-10 01:07:34.864479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87596009c88e'
down_revision = 'aed2d873ca8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('note', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_column('note')
        batch_op.drop_column('image')

    # ### end Alembic commands ###