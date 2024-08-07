from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    role: int


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
