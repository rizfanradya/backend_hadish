from pydantic import BaseModel


class CreateAndUpdateTypeHadith(BaseModel):
    type: str
