"""Acceptance tests written in a Given-When-Then (BDD) style.

Each test maps directly to a user story acceptance criterion in
docs/user_stories.md. They exercise the app end-to-end through the HTTP layer,
the way a real member would, rather than testing internals — validating that we
built the *right* thing, not just that the code runs.
"""
from datetime import datetime, timedelta

from app.extensions import db
from app.models import User, Event
from tests.conftest import login


def test_new_member_can_sign_up_and_reach_dashboard(client, app):
    """
    As a new visitor I want to register so that I can join events.
      Given I am not registered
      When I submit the registration form with valid details
      Then I should be logged in and see my dashboard
    """
    resp = client.post(
        "/register",
        data={
            "username": "amara",
            "email": "amara@example.com",
            "password": "runfast1",
            "confirm": "runfast1",
        },
        follow_redirects=True,
    )
    assert b"Hi amara" in resp.data  # dashboard greeting


def test_member_can_join_event_and_see_it_on_dashboard(client, app):
    """
    As a member I want to RSVP to an event so that my place is saved
    and the session appears among my upcoming sessions.
      Given a published upcoming event exists
      When I RSVP to it
      Then it appears in 'Your upcoming sessions' on my dashboard
    """
    with app.app_context():
        host = User(username="host", email="host@example.com")
        host.set_password("password123")
        member = User(username="member", email="member@example.com")
        member.set_password("password123")
        db.session.add_all([host, member])
        db.session.commit()
        event = Event(
            title="Sunset Yoga",
            description="Wind down.",
            location="Beach",
            category="Yoga",
            starts_at=datetime.utcnow() + timedelta(days=1),
            capacity=10,
            organiser_id=host.id,
        )
        db.session.add(event)
        db.session.commit()
        event_id = event.id

    login(client, email="member@example.com")
    client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    resp = client.get("/dashboard")
    assert b"Sunset Yoga" in resp.data


def test_member_receives_reminder_after_rsvp(client, app):
    """
    As a member I want a reminder when I join an event so that I
    don't forget to attend.
      Given I am a logged-in member
      When I RSVP to an event
      Then a reminder notification is shown on my dashboard
    """
    with app.app_context():
        host = User(username="host2", email="host2@example.com")
        host.set_password("password123")
        member = User(username="mem2", email="mem2@example.com")
        member.set_password("password123")
        db.session.add_all([host, member])
        db.session.commit()
        event = Event(
            title="Trail Run",
            description="10k.",
            location="Forest",
            category="Running",
            starts_at=datetime.utcnow() + timedelta(days=2),
            capacity=10,
            organiser_id=host.id,
        )
        db.session.add(event)
        db.session.commit()
        event_id = event.id

    login(client, email="mem2@example.com")
    client.post(f"/events/{event_id}/rsvp", follow_redirects=True)
    resp = client.get("/dashboard")
    assert b"You joined" in resp.data  # reminder text in notification feed
