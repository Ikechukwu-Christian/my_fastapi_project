# models.py

from pydantic import BaseModel

class EventBooking(BaseModel):
    attendee_name: str
    attendee_email: str
    attendee_age: int
    event_name: str
    event_date: str
    event_location: str
    ticket_type: str
 

