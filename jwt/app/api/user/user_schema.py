from pydantic import BaseModel
from typing import Optional
class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "email": "oHc9t@example.com",
                "password": "password123"
            }
        }
    }


class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    
class LoginUser(BaseModel):
    email: str
    password: str
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "oHc9t@example.com",
                "password": "password123"
            }
        }
    }    