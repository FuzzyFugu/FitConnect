"""Database models for FitConnect.

Three core entities model the MVP domain:
  * User  - a registered member who can create events and RSVP.
  * Event - a fitness meetup (run, yoga class, group hike, etc.).
  * RSVP  - the join/cancel relationship between a user and an event.
  * Notification - in-app reminder feed entries.
"""
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Flask-Login callback used to reload the user from the session."""
    return db.session.get(User, int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    events = db.relationship("Event", backref="organiser", lazy=True)
    rsvps = db.relationship("RSVP", backref="user", lazy=True)
    notifications = db.relationship("Notification", backref="user", lazy=True)

    def set_password(self, password):
        """Store a salted hash rather than the raw password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(140), nullable=False)
    category = db.Column(db.String(60), nullable=False)  # e.g. Running, Yoga, Hiking
    starts_at = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, default=20)
    organiser_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    rsvps = db.relationship(
        "RSVP", backref="event", lazy=True, cascade="all, delete-orphan"
    )

    @property
    def attendee_count(self):
        return len(self.rsvps)

    @property
    def is_full(self):
        return self.attendee_count >= self.capacity

    @property
    def is_upcoming(self):
        return self.starts_at >= datetime.utcnow()

    def __repr__(self):
        return f"<Event {self.title}>"


class RSVP(db.Model):
    __tablename__ = "rsvps"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # A user can only RSVP once per event.
    __table_args__ = (
        db.UniqueConstraint("user_id", "event_id", name="uq_user_event"),
    )


class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
