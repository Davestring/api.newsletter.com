"""empty message

Revision ID: 7f6014232f4f
Revises: e6e33762627d
Create Date: 2023-04-10 09:26:19.323037

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "7f6014232f4f"
down_revision = "e6e33762627d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "attachments",
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column("mimetype", sa.String(length=32), nullable=False),
        sa.Column("file", sa.LargeBinary(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("newsletters", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("attachment_id", sa.UUID(), nullable=True)
        )
        batch_op.create_foreign_key(
            None, "attachments", ["attachment_id"], ["id"]
        )
        batch_op.drop_column("attachment")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("newsletters", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "attachment",
                postgresql.BYTEA(),
                autoincrement=False,
                nullable=True,
            )
        )
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("attachment_id")

    op.drop_table("attachments")
    # ### end Alembic commands ###
