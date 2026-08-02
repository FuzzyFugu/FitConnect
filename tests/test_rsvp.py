"""Unit tests for the RSVP system including capacity enforcement."""
from datetime import datetime, timedelta

from app.extensions import db
from app.models import Event, RSVP, User
from tests.conftest import login


def _make_event(app, capacity=2):
    with app.app_context():
        organiser = User(username="host", email="host@example.com")
        organiser.set_password("password123")
        db.session.add(organiser)
        db.session.commit()
        event = Event(
            title="Group Hike",
            description="6 mile loop.",
            location="Hill Trail",
            category="Hiking",
            starts_at=datetime.utcnow() + timedelta(days=5),
            capacity=capacity,
            organiser_id=organiser.id,
        )
        db.session.add(event)
        db.session.commit()
        return event.id


def test_user_can_rsvp(client, user, app):
    event_id = _make_event(app)
    login(client)
    resp = client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    assert b"See you there" in resp.data
    with app.app_context():
        assert RSVP.query.filter_by(event_id=event_id).count() == 1


def test_user_can_cancel_rsvp(client, user, app):
    event_id = _make_event(app)
    login(client)
    client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    resp = client.post(f"/events/{event_id}/cancel", follow_redirects=True)
    assert b"cancelled" in resp.data
    with app.app_context():
        assert RSVP.query.filter_by(event_id=event_id).count() == 0


def test_capacity_is_enforced(client, app):
    event_id = _make_event(app, capacity=1)

    # First user fills the single slot.
    with app.app_context():
        u1 = User(username="u1", email="u1@example.com")
        u1.set_password("password123")
        u2 = User(username="u2", email="u2@example.com")
        u2.set_password("password123")
        db.session.add_all([u1, u2])
        db.session.commit()

    login(client, email="u1@example.com")
    client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    client.get("/logout")

    # Second user should be blocked because the event is full.
    login(client, email="u2@example.com")
    resp = client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    assert b"full" in resp.data
    with app.app_context():
        assert RSVP.query.filter_by(event_id=event_id).count() == 1
