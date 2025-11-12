import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "message" in data
    assert "Flask" in data["message"]

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_add_success(client):
    resp = client.get("/add?a=2&b=3")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["sum"] == 5.0

def test_add_missing_params(client):
    resp = client.get("/add?a=2")
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data
    
