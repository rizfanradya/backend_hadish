from pydantic import BaseModel


class CreateAndUpdateUser(BaseModel):
    created_by: int
    updated_by: int
    username: str
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
