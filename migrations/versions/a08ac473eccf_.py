"""empty message

Revision ID: a08ac473eccf
Revises: 8e04db7911e7
Create Date: 2020-01-31 01:19:04.268478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08ac473eccf'
down_revision = '8e04db7911e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=1000), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('lawyer', sa.Column('phone', sa.String(length=120), nullable=False))
    op.drop_index('password', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('password', 'user', ['password'], unique=True)
    op.drop_column('lawyer', 'phone')
    op.drop_table('question')
    # ### end Alembic commands ###
