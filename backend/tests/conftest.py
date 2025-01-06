import pytest
from app import create_app, db


@pytest.fixture
def app():
    """Create and configure a new app instance for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.drop_all()  # Drop all tables before creating
        db.create_all()  # Create fresh tables for testing
        yield app
        db.session.remove()
        db.drop_all()



@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
