from pydantic import BaseModel


class CreateAndUpdateHadith(BaseModel):
    created_by: int
    updated_by: int
    hadith: str
    explanation: str
