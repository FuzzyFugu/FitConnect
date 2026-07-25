"""Application factory.

Using the factory pattern makes the app easy to configure per environment and
straightforward to test (each test can build an isolated app instance).
"""
from flask import Flask

from config import Config
from app.extensions import db, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialise extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints (feature modules)
    from app.main.routes import main_bp

    app.register_blueprint(main_bp)

    # Create tables on first run for the SQLite MVP database.
    with app.app_context():
        db.create_all()

    return app
