"""empty message

Revision ID: 97d37cb3f0c6
Revises: 
Create Date: 2024-04-07 20:37:49.971138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d37cb3f0c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('event_type_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_events_categories_events', 'categories_events', ['event_type_id'], ['id'])

    with op.batch_alter_table('places', schema=None) as batch_op:
        batch_op.add_column(sa.Column('etat_place', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('places', schema=None) as batch_op:
        batch_op.drop_column('etat_place')

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('event_type_id')

    # ### end Alembic commands ###
