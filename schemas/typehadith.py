from pydantic import BaseModel


class CreateAndUpdateTypeHadith(BaseModel):
    created_by: int
    updated_by: int
    type: str
