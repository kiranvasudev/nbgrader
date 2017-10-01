"""a description of the change

Revision ID: 231cd27152c1
Revises: 724cde206c17
Create Date: 2017-09-13 10:11:05.150429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '231cd27152c1'
down_revision = '724cde206c17'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('comment', Column('rubric-checkbox-state', Boolean))
    op.add_column('comment', Column('rubric-grade', Float))
    op.add_column('comment', Column('rubric-information', String))
    pass


def downgrade():
    op.drop_column('comment', 'rubric-checkbox-state')
    op.drop_column('comment', 'rubric-grade')
    op.drop_column('comment', 'rubric-information')
    pass
