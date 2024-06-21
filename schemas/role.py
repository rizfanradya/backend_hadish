from pydantic import BaseModel


class CreateAndUpdateRole(BaseModel):
    created_by: int
    updated_by: int
    role: str
