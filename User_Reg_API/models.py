from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic import BaseModel, Field, EmailStr, validator
import bcrypt

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=8, description="Password of the user")

    @validator('password')
    def validate_password(cls, value):
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in value):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit')
        return value

    

# class UserRegistration(BaseModel):
#     name: str = Field(min_length=3, max_length=50, description="Name of the passenger", examples=["John Doe"], title="Name",pattern="^[a-zA-Z ]+$")  # noqa
#     age: int = Field(gt=0, lt=120, description="Age of the passenger", examples=[25], title="Age") # noqa
#     email: EmailStr
#     phone: PhoneNumber = Field(description="Phone number of the passenger", examples=["+2348123456789"], title="Phone Number")  # noqa
    
#     password: str = Field(..., min_length=8, description="Password of the user")

class Responses(BaseModel):
    status_code: int
    data: dict
    message: str
    



