"""Create user_profile  table

Revision ID: 33312944bfab
Revises: d1f0cf8c5671
Create Date: 2023-10-25 00:59:21.581079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33312944bfab'
down_revision = 'd1f0cf8c5671'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
