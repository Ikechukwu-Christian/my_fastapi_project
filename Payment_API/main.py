# Payment Processing API:
# ● Build a FastAPI route for processing payments.
# ● Utilize request body parameters for payment amount, card number, expiration
# date, and CVV.
# ● Implement numeric validation for payment amount and card-related fields.
# ● Validate expiration date format and ensure it's not expired.
# ● Simulate payment processing logic (e.g., validation, authentication) within the
# route.
# ● Test the API with valid and invalid payment data.

from fastapi import FastAPI, HTTPException
from models import Payment

app = FastAPI()

@app.post("/process-payment/")
async def process_payment(payment: Payment):
    # Validate payment amount
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="Payment amount must be greater than zero")

    # Validate card number (just numeric)
    if not payment.card_number.isnumeric():
        raise HTTPException(status_code=400, detail="Card number must contain only numeric characters")

    # Validate expiration date format (MM/YY)
    try:
        exp_month, exp_year = payment.expiration_date.split('/')
        exp_month = int(exp_month)
        exp_year = int(exp_year)
        if not (1 <= exp_month <= 12):
            raise ValueError
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Invalid expiration date format (MM/YY)")

    # Validate expiration date is not expired
    # Assume current date is 03/24
    current_month = 3
    current_year = 24
    if exp_year > current_year or (exp_year == current_year and exp_month > current_month):
        raise HTTPException(status_code=400, detail="Card is expired")

    # Validate CVV (just numeric)
    if not payment.cvv.isnumeric():
        raise HTTPException(status_code=400, detail="CVV must contain only numeric characters")

    return {"message": "Payment processed successfully"}
