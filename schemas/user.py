from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    created_by: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    role: Optional[int]


class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    status: bool
    role: int


class UserLogin(BaseModel):
    email: str
    password: str
