from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/filmes")
    assert response.status_code == 200

def test_crud():
    response = client.put("/filmes/teste")
    assert response.status_code == 200