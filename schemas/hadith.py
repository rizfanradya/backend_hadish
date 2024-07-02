from pydantic import BaseModel
from typing import Optional


class CreateAndUpdateHadith(BaseModel):
    created_by: int
    updated_by: int
    hadith: str
    explanation: str
    type_hadith: Optional[int]
