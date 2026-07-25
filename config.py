"""Application configuration.

Centralises all environment-driven settings so that the same codebase can run
locally (SQLite) or in a hosted environment without code changes.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Secret key protects sessions and CSRF tokens. Override in production.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")

    # Database: defaults to a local SQLite file for zero-config development.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "fitconnect.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Notification delivery. When MAIL_ENABLED is false (default) reminders are
    # written to the in-app notification feed only, keeping the MVP dependency-free.
    MAIL_ENABLED = os.environ.get("MAIL_ENABLED", "false").lower() == "true"


class TestConfig(Config):
    """Configuration used by the automated test suite."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
