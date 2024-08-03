from pydantic import BaseModel


class CreateAndUpdateRole(BaseModel):
    role: str
