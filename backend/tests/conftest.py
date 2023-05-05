# tests/conftest.py
import pytest
from backend.src.server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
