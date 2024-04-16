from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_vehicle_by_id():
    response = client.get("/vehicles/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "make": "Toyota", "model": "Corolla", "price": 15000.0}

def test_get_vehicle_by_invalid_id():
    response = client.get("/vehicles/100")
    assert response.status_code == 404

def test_get_vehicles_by_make():
    response = client.get("/vehicles/?make=Toyota")
    assert response.status_code == 200
    assert len(response.json()) == 1