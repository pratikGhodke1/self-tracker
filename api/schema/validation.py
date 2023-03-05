"""Request validation models"""

# pylint: disable=no-name-in-module
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserPostRequest(BaseModel):
    """User POST request validation model"""

    first_name: str
    last_name: Optional[str] = ""
    password: str
    birth_date: str
    email: EmailStr
    mobile: str = Field(max_length=10, min_length=10)


class UserPutRequest(BaseModel):
    """User PUT request validation model"""

    first_name: Optional[str]
    last_name: Optional[str] = ""
    password: Optional[str]
    birth_date: Optional[str]
    email: Optional[EmailStr]
    mobile: Optional[str] = Field(max_length=10, min_length=10)
