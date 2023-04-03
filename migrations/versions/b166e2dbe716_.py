"""empty message

Revision ID: b166e2dbe716
Revises:
Create Date: 2023-04-03 01:50:28.146656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b166e2dbe716"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contacts",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("last_name", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contacts")
    # ### end Alembic commands ###