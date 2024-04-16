from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_book_event_valid():
    payload = {
        "attendee_name": "Idan",
        "attendee_email": "idan@yahoo.com",
        "attendee_age": 30,
        "event_name": "Concert",
        "event_date": "2024-05-15",
        "event_location": "New York",
        "ticket_type": "VIP"
    }
    response = client.post("/book-event/", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Booking confirmed for Idan for Concert"

def test_book_event_invalid_age():
    payload = {
        "attendee_name": "Idan",
        "attendee_email": "idan@yahoo.co",
        "attendee_age": -10,
        "event_name": "Workshop",
        "event_date": "2024-06-20",
        "event_location": "Enugu",
        "ticket_type": "General"
    }
    response = client.post("/book-event/", json=payload)
    assert response.status_code == 400



