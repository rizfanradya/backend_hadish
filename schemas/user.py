from pydantic import BaseModel


class CreateAndUpdateUser(BaseModel):
    username: str = 'username'
    email: str = 'email@gmail.com'
    password: str = 'password'
    confirm_password: str = 'password'
    status: bool = True
    role: int = 1


class UserLogin(BaseModel):
    username: str
    password: str
