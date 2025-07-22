import pytest
from app import app, db

@pytest.fixture
def client():
    # configure the app for testing
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    # create a test client
    with app.test_client() as client:
        # create the database and tables
        with app.app_context():
            db.create_all()
        
        yield client

        # teardown the database
        with app.app_context():
            db.drop_all()
