import os
import pytest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app
from app.config import DevelopmentConfig

@pytest.fixture
def client() -> FlaskClient:
    os.environ["FLASK_ENV"] = "development"
    app: Flask = create_app(DevelopmentConfig)
    app.testing = True
    with app.test_client() as client:
        yield client
