"""Bulk resources module."""
import csv
import io

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from app.contact import Contact
from app.newsletter_type import NewsletterType
from app.subscription import Subscription
from utils import ListResource, db

from .models import Bulk
from .schemas import BulkSchema


class BulkResource(Resource):
    """Manage single bulk resources.

    Attributes
    ----------
    schema : BulkSchema
        Serialization schema object.

    Methods
    -------
    post()
        Create a bulk of contact registries and store the bulk history.

    """

    schema = BulkSchema()

    def post(self):
        """Create a bulk of contact registries and store the bulk history."""
        data = request.form.to_dict()
        try:
            serialized_data = self.schema.load(data)
        except ValidationError as e:
            return e.messages, 400

        file = request.files.get("csv")
        if file is None:
            return {"csv": ["Missing data for required field."]}, 400

        bulk = Bulk.find_by_name(serialized_data["name"])
        if bulk is not None:
            return {
                "message": f"A registry with the name '{bulk.name}' already exists."
            }, 403

        try:
            bulk = Bulk(**serialized_data)
            bulk.save()
        except:
            return {
                "message": "An error occurred during CREATE operation."
            }, 500

        # TODO: move the following code to an async task.
        # TODO: find a way to make a cleaner solution for this algorithm.

        reader = csv.reader(io.TextIOWrapper(file))
        next(reader)

        for name, last_name, email in reader:
            try:
                contact = Contact(
                    name=name,
                    last_name=last_name,
                    email=email,
                    bulk_id=bulk.id,
                )
                contact.save()

                newsletter_types = NewsletterType.find_all()
                for newsletter_type in newsletter_types:
                    subscription = Subscription(
                        contact_id=contact.id,
                        newsletter_type_id=newsletter_type.id,
                        is_active=True,
                    )
                    subscription.save()
            except:
                db.session.rollback()
                setattr(bulk, "errors", bulk.errors + 1)
                bulk.update()

        try:
            contacts = Contact.find_by_bulk_id(bulk.id)
            setattr(bulk, "inserted", contacts.count())

            bulk.update()
        except Exception as e:
            pass

        return self.schema.dump(bulk), 201


class BulkListResource(ListResource):
    """Extends from `ListResource` and manage a list of bulks."""

    model = Bulk
    schema_class = BulkSchema


__all__ = ["BulkResource", "BulkListResource"]
