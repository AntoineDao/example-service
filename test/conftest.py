import os
import pytest

from app import create_app
from app.resources.database import db


@pytest.fixture
def app():
    app = create_app(config='test')
    
    with app.app_context():   
        db.create_all()
        yield app   # Note that we changed return for yield, see below for why
        db.session.commit()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
