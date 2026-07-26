"""Unit tests for the authentication flow (registration, login, logout)."""
from app.models import User


def test_password_is_hashed_not_stored_plaintext(user):
    assert user.password_hash != "password123"
    assert user.check_password("password123")
    assert not user.check_password("wrongpassword")


def test_register_creates_user(client, app):
    resp = client.post(
        "/register",
        data={
            "username": "newbie",
            "email": "newbie@example.com",
            "password": "secret123",
            "confirm": "secret123",
        },
        follow_redirects=True,
    )
    assert resp.status_code == 200
    with app.app_context():
        assert User.query.filter_by(email="newbie@example.com").first() is not None


def test_register_rejects_duplicate_email(client, user):
    resp = client.post(
        "/register",
        data={
            "username": "different",
            "email": "tester@example.com",
            "password": "secret123",
            "confirm": "secret123",
        },
        follow_redirects=True,
    )
    assert b"already exists" in resp.data


def test_login_with_valid_credentials(client, user):
    resp = client.post(
        "/login",
        data={"email": "tester@example.com", "password": "password123"},
        follow_redirects=True,
    )
    assert b"Dashboard" in resp.data


def test_login_with_invalid_password_fails(client, user):
    resp = client.post(
        "/login",
        data={"email": "tester@example.com", "password": "wrong"},
        follow_redirects=True,
    )
    assert b"Invalid email or password" in resp.data
