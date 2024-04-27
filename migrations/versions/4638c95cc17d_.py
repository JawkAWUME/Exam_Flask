"""empty message

Revision ID: 4638c95cc17d
Revises: 87596009c88e
Create Date: 2024-04-11 10:36:37.398487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4638c95cc17d'
down_revision = '87596009c88e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salle_id', sa.Integer(), nullable=True))

        batch_op.add_column(sa.Column('tour_id', sa.Integer(), nullable=True))
        batch_op.alter_column('note',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
        batch_op.create_foreign_key('fk_event_tour', 'tours', ['tour_id'], ['id'])
        batch_op.create_foreign_key('fk_event_salle', 'salles', ['salle_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('note',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.drop_column('tour_id')
        batch_op.drop_column('salle_id')

    # ### end Alembic commands ###