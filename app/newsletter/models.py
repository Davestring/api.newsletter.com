"""Newsletter models module."""
from typing import Optional

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from utils import BaseModel, db


class Newsletter(db.Model, BaseModel):
    """Declaration of the Newsletter model.

    Attributes
    ----------
    subject : Column
        Newsletter subject message, this field is required.
    attachment_id : Column
        Foreign key to an attachment registry, this field is optional.
    template_id : Column
        Foreign key of a template registry, this field is optional.
    newsletter_type_id : Column
        Foreign key of a newsletter-type registry, this field is required.

    """

    __tablename__ = "newsletters"

    subject = Column(String(256), nullable=False)

    attachment_id = Column(
        UUID(as_uuid=True), ForeignKey("attachments.id"), nullable=True
    )
    template_id = Column(
        UUID(as_uuid=True), ForeignKey("templates.id"), nullable=True
    )
    newsletter_type_id = Column(
        UUID(as_uuid=True), ForeignKey("newsletter_type.id"), nullable=False
    )

    @classmethod
    def find_by_id(self, _id: str) -> Optional["Newsletter"]:
        """Query a single resource by the given id."""
        return self.query.filter_by(id=_id).first()

    def save(self):
        """Create a new resource."""
        db.session.add(self)
        db.session.commit()


__all__ = ["Newsletter"]
