"""Main routes: landing page and the member dashboard.

The dashboard aggregates the sessions a user has RSVP'd to plus the events they
organise, and surfaces their unread in-app notifications — the single view a
returning member lands on.
"""
from datetime import datetime

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import Event, RSVP, Notification
from app.extensions import db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    # Show a teaser of the next few events to logged-out visitors.
    upcoming = (
        Event.query.filter(Event.starts_at >= datetime.utcnow())
        .order_by(Event.starts_at.asc())
        .limit(3)
        .all()
    )
    return render_template("index.html", events=upcoming)


@main_bp.route("/dashboard")
@login_required
def dashboard():
    # Sessions the user is attending (upcoming only).
    attending = (
        Event.query.join(RSVP, RSVP.event_id == Event.id)
        .filter(RSVP.user_id == current_user.id, Event.starts_at >= datetime.utcnow())
        .order_by(Event.starts_at.asc())
        .all()
    )
    # Events the user organises.
    organising = (
        Event.query.filter_by(organiser_id=current_user.id)
        .order_by(Event.starts_at.asc())
        .all()
    )
    notifications = (
        Notification.query.filter_by(user_id=current_user.id)
        .order_by(Notification.created_at.desc())
        .limit(10)
        .all()
    )
    # Mark unread notifications as read now they've been displayed.
    for note in notifications:
        note.is_read = True
    db.session.commit()

    return render_template(
        "dashboard.html",
        attending=attending,
        organising=organising,
        notifications=notifications,
    )
