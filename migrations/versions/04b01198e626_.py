"""empty message

Revision ID: 04b01198e626
Revises: 
Create Date: 2020-09-06 22:05:25.803893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04b01198e626'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###