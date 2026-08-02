"""Notification service.

Encapsulates reminder delivery so the rest of the app doesn't care *how* a
notification is sent. For the MVP we always write an in-app notification; if
MAIL_ENABLED is configured the same message is also dispatched by email.
Keeping this behind a single function makes it trivial to swap in a real email
provider (SendGrid, SES) later without touching the route handlers.
"""
from flask import current_app

from app.extensions import db
from app.models import Notification


def notify(user, message):
    """Create an in-app notification and optionally send an email."""
    note = Notification(user_id=user.id, message=message)
    db.session.add(note)
    db.session.commit()

    if current_app.config.get("MAIL_ENABLED"):
        _send_email(user.email, message)

    return note


def _send_email(address, message):
    """Placeholder email dispatch.

    Intentionally a stub for the MVP — logging keeps the demo dependency-free
    while documenting the integration point for a production email backend.
    """
    current_app.logger.info("EMAIL to %s: %s", address, message)
