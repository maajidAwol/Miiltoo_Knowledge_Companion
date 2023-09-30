"""change type

Revision ID: 431be2f1326b
Revises: 408f11b7625a
Create Date: 2023-09-29 00:19:20.855603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431be2f1326b'
down_revision = '408f11b7625a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('verification_code',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=4),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('verification_code',
               existing_type=sa.String(length=4),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###