import pytest

from app import create_app
from app.extensions import db
from app.models import User
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user(app):
    """A ready-made registered user."""
    u = User(username="tester", email="tester@example.com")
    u.set_password("password123")
    db.session.add(u)
    db.session.commit()
    return u


def login(client, email="tester@example.com", password="password123"):
    """Helper to authenticate the test client."""
    return client.post(
        "/login", data={"email": email, "password": password}, follow_redirects=True
    )
