# models.py

from pydantic import BaseModel

class Payment(BaseModel):
    amount: float
    card_number: str
    expiration_date: str
    cvv: str
