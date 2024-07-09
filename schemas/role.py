from pydantic import BaseModel


class CreateAndUpdateRole(BaseModel):
    created_by: int
    role: str
