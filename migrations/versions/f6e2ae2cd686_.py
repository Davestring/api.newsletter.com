"""empty message

Revision ID: f6e2ae2cd686
Revises: b6f0073c9487
Create Date: 2023-04-09 15:08:11.077029

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "f6e2ae2cd686"
down_revision = "b6f0073c9487"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contacts_subscriptions")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contacts_subscriptions",
        sa.Column(
            "contact_id", sa.UUID(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "subscription_id", sa.UUID(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "is_subscribed", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["contact_id"],
            ["contacts.id"],
            name="contacts_subscriptions_contact_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["subscription_id"],
            ["subscriptions.id"],
            name="contacts_subscriptions_subscription_id_fkey",
        ),
        sa.PrimaryKeyConstraint(
            "contact_id", "subscription_id", name="contacts_subscriptions_pkey"
        ),
    )
    # ### end Alembic commands ###
