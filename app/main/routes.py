"""Main routes: landing page (dashboard is added once accounts exist)."""
from datetime import datetime

from flask import Blueprint, render_template

from app.models import Event

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    upcoming = (
        Event.query.filter(Event.starts_at >= datetime.utcnow())
        .order_by(Event.starts_at.asc())
        .limit(3)
        .all()
    )
    return render_template("index.html", events=upcoming)
