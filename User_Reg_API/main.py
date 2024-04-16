# User Registration API:
# ● Create a FastAPI route for user registration.
# ● Use request body parameters for username, email, and password.
# ● Implement string validation for username and email.
# ● Ensure password meets certain complexity requirements.
# ● Return appropriate error messages for invalid inputs.
# ● Simulate registration process with FastAPI TestClient.


from fastapi import FastAPI
from routes import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])



