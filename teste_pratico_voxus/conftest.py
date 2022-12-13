import pytest
from teste_pratico_voxus.app import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    _client = TestClient(app)
    yield _client
