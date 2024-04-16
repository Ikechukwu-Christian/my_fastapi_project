from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_payment_invalid_amount():
    payload = {
        "amount": -50.0,
        "card_number": "1234567890123456",
        "expiration_date": "12/25",
        "cvv": "123"
    }
    response = client.post("/process-payment/", json=payload)
    assert response.status_code == 400

def test_process_payment_invalid_card_number():
    payload = {
        "amount": 100.0,
        "card_number": "1234567a89012345",
        "expiration_date": "12/25",
        "cvv": "123"
    }
    response = client.post("/process-payment/", json=payload)
    assert response.status_code == 400