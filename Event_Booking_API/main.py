# Event Booking API:
# ● Build a FastAPI endpoint for booking events (e.g., concerts, workshops).
# ● Use request body parameters for attendee information (name, email, age), event
# details (name, date, location), and ticket type.
# ● Implement string validation for attendee details and event name.
# ● Apply numeric validation for attendee age.
# ● Validate ticket type against available options.
# ● Return booking confirmation with event details.
# ● Test the API with various scenarios, including full and partial book

from fastapi import FastAPI, HTTPException
from models import EventBooking

app = FastAPI()

# Mock event booking function
def book_event(booking_details: EventBooking):
    # Simulate event booking process
    # Here you would typically perform validation, authentication, and store booking details in a database
    return {"message": f"Booking confirmed for {booking_details.attendee_name} for {booking_details.event_name}"}

@app.post("/book-event/")
async def book_event_route(booking_details: EventBooking):
    # Validate attendee age
    if booking_details.attendee_age <= 0:
        raise HTTPException(status_code=400, detail="Attendee age must be greater than zero")

    # Validate ticket type
    valid_ticket_types = ["VIP", "General", "Student"]
    if booking_details.ticket_type not in valid_ticket_types:
        raise HTTPException(status_code=400, detail="Invalid ticket type")

    # Perform event booking
    confirmation = book_event(booking_details)
    return confirmation
