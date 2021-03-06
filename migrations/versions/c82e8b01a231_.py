"""empty message

Revision ID: c82e8b01a231
Revises: 7608ebbc17b3
Create Date: 2020-08-16 21:54:14.162709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c82e8b01a231'
down_revision = '7608ebbc17b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teams', sa.Column('abbreviation', sa.String(length=5), nullable=True))
    op.add_column('teams', sa.Column('alternateColor', sa.String(length=20), nullable=True))
    op.add_column('teams', sa.Column('color', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teams', 'color')
    op.drop_column('teams', 'alternateColor')
    op.drop_column('teams', 'abbreviation')
    # ### end Alembic commands ###
