from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_predict():
    payload = {
        "comments": "Glowing disc in the night sky",
        "duration_seconds": 60,
        "country": "us",
        "year": 2024,
        "month": 5,
        "hour": 21,
        "desc_length": 28
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_shape" in response.json()
