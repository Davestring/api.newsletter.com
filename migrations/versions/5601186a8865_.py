"""empty message

Revision ID: 5601186a8865
Revises: c0239514fc05
Create Date: 2023-04-06 01:08:00.828232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5601186a8865"
down_revision = "c0239514fc05"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("contacts", schema=None) as batch_op:
        batch_op.add_column(sa.Column("bulk_id", sa.UUID(), nullable=True))
        batch_op.create_foreign_key(None, "bulks", ["bulk_id"], ["id"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("contacts", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("bulk_id")

    # ### end Alembic commands ###