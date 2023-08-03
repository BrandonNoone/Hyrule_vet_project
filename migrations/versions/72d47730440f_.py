"""empty message

Revision ID: 72d47730440f
Revises: ddb54ba82a2e
Create Date: 2023-08-01 14:21:19.545902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d47730440f'
down_revision = 'ddb54ba82a2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.drop_column('age')

    # ### end Alembic commands ###