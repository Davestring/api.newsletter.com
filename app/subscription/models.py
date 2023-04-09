"""Subscription models module."""
from sqlalchemy import UUID, Boolean, Column, ForeignKey

from utils import BaseModel, db


class Subscription(db.Model, BaseModel):
    """Declaration of the Subscription model.

    Attributes
    ----------
    contact_id : Column
        Foreign key of a contact registry, this field is required.
    newsletter_type_id : Column
        Foreign key of a newsletter-type registry, this field is required.
    is_active : Column
        If `true`, it means that this contact will receive newsletters related
        to the newsletter-type, default is `True`.

    """

    __tablename__ = "subscriptions"

    contact_id = Column(
        UUID(as_uuid=True), ForeignKey("contacts.id"), nullable=True
    )
    newsletter_type_id = Column(
        UUID(as_uuid=True), ForeignKey("newsletter_type.id"), nullable=True
    )
    is_active = Column(Boolean, default=True, nullable=False)


__all__ = ["Subscription"]
