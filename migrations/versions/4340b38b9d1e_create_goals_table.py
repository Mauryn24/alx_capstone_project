"""Create goals table

Revision ID: 4340b38b9d1e
Revises: 
Create Date: 2023-10-23 23:19:37.759288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4340b38b9d1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    op.drop_table('goals')
    # ### end Alembic commands ###