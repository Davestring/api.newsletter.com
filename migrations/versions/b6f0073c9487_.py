"""empty message

Revision ID: b6f0073c9487
Revises: 5601186a8865
Create Date: 2023-04-06 01:39:41.899265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b6f0073c9487"
down_revision = "5601186a8865"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("bulks", schema=None) as batch_op:
        batch_op.drop_column("repeated")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("bulks", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "repeated", sa.INTEGER(), autoincrement=False, nullable=True
            )
        )

    # ### end Alembic commands ###