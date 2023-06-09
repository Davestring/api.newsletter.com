"""empty message

Revision ID: c8aaf0ab9eec
Revises:
Create Date: 2023-04-04 03:01:10.832233

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c8aaf0ab9eec"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contacts",
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("last_name", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
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
