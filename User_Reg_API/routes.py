from fastapi import APIRouter, HTTPException
from models import UserRegistration
from fastapi.responses import JSONResponse
from models import Responses 
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(self):
        # Hash the password using bcrypt
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), salt).decode('utf-8')

# Example usage
# try:
#     user_data = UserRegistration(username="john_doe", email="john@example.com", password="Passw0rd")
#     user_data.hash_password()
#     print("User registration data is valid.")
#     print("Hashed password:", user_data.password)
# except ValueError as e:
#     print(e)


@router.post("/register", response_model=Responses)
async def user_registration(user: UserRegistration):
    try:
        hash_password = pwd_context.hash(user.password)
        user_data = {
            'username': user.username,
            'password': hash_password,
            'email': user.email
        }
        results = user_data
        # return user_data
        return JSONResponse(status_code=201, content={"data": results, "message": "User Registration successful"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
