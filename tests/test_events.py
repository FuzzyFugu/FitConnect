"""Unit tests for event creation and editing."""
from datetime import datetime, timedelta

from app.models import Event
from tests.conftest import login


def test_create_event(client, user, app):
    login(client)
    future = (datetime.utcnow() + timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")
    resp = client.post(
        "/events/new",
        data={
            "title": "Sunrise 5k",
            "description": "Easy paced group run.",
            "location": "Riverside Park",
            "category": "Running",
            "starts_at": future,
            "capacity": 15,
        },
        follow_redirects=True,
    )
    assert resp.status_code == 200
    with app.app_context():
        event = Event.query.filter_by(title="Sunrise 5k").first()
        assert event is not None
        assert event.capacity == 15


def test_only_organiser_can_edit(client, app):
    from app.extensions import db
    from app.models import User

    # Two users: organiser and an outsider.
    with app.app_context():
        organiser = User(username="org", email="org@example.com")
        organiser.set_password("password123")
        outsider = User(username="out", email="out@example.com")
        outsider.set_password("password123")
        db.session.add_all([organiser, outsider])
        db.session.commit()
        event = Event(
            title="Yoga in the park",
            description="Bring a mat.",
            location="Green Square",
            category="Yoga",
            starts_at=datetime.utcnow() + timedelta(days=2),
            capacity=20,
            organiser_id=organiser.id,
        )
        db.session.add(event)
        db.session.commit()
        event_id = event.id

    login(client, email="out@example.com")
    resp = client.get(f"/events/{event_id}/edit")
    assert resp.status_code == 403
