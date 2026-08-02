"""Event and RSVP routes.

Owned by the Backend developer. Implements:
  * Create / edit events (organiser only)
  * Browse all upcoming events
  * RSVP join / cancel with capacity enforcement
Each state change triggers an in-app notification via the notification service.
"""
from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from app.extensions import db
from app.models import Event, RSVP
from app.events.forms import EventForm
from app.notifications.service import notify

events_bp = Blueprint("events", __name__)


@events_bp.route("/events")
def list_events():
    """Public listing of every upcoming event, soonest first."""
    upcoming = (
        Event.query.filter(Event.starts_at >= db.func.now())
        .order_by(Event.starts_at.asc())
        .all()
    )
    return render_template("events/list.html", events=upcoming)


@events_bp.route("/events/<int:event_id>")
def detail(event_id):
    event = db.get_or_404(Event, event_id)
    user_rsvped = False
    if current_user.is_authenticated:
        user_rsvped = (
            RSVP.query.filter_by(user_id=current_user.id, event_id=event.id).first()
            is not None
        )
    return render_template("events/detail.html", event=event, user_rsvped=user_rsvped)


@events_bp.route("/events/new", methods=["GET", "POST"])
@login_required
def create():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            location=form.location.data,
            category=form.category.data,
            starts_at=form.starts_at.data,
            capacity=form.capacity.data,
            organiser_id=current_user.id,
        )
        db.session.add(event)
        db.session.commit()
        flash("Event created!", "success")
        return redirect(url_for("events.detail", event_id=event.id))
    return render_template("events/form.html", form=form, heading="Create event")


@events_bp.route("/events/<int:event_id>/edit", methods=["GET", "POST"])
@login_required
def edit(event_id):
    event = db.get_or_404(Event, event_id)
    # Only the organiser may edit their own event.
    if event.organiser_id != current_user.id:
        abort(403)

    form = EventForm(obj=event)
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.commit()
        flash("Event updated.", "success")
        return redirect(url_for("events.detail", event_id=event.id))
    return render_template("events/form.html", form=form, heading="Edit event")


@events_bp.route("/events/<int:event_id>/rsvp", methods=["POST"])
@login_required
def rsvp(event_id):
    event = db.get_or_404(Event, event_id)

    existing = RSVP.query.filter_by(user_id=current_user.id, event_id=event.id).first()
    if existing:
        flash("You are already signed up for this event.", "info")
        return redirect(url_for("events.detail", event_id=event.id))

    if event.is_full:
        flash("Sorry, this event is full.", "warning")
        return redirect(url_for("events.detail", event_id=event.id))

    db.session.add(RSVP(user_id=current_user.id, event_id=event.id))
    db.session.commit()
    notify(current_user, f"You joined '{event.title}' on {event.starts_at:%d %b %H:%M}.")
    flash("You're in! See you there.", "success")
    return redirect(url_for("events.detail", event_id=event.id))


@events_bp.route("/events/<int:event_id>/cancel", methods=["POST"])
@login_required
def cancel(event_id):
    event = db.get_or_404(Event, event_id)
    existing = RSVP.query.filter_by(user_id=current_user.id, event_id=event.id).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        notify(current_user, f"You cancelled your place at '{event.title}'.")
        flash("Your RSVP has been cancelled.", "info")
    return redirect(url_for("events.detail", event_id=event.id))
