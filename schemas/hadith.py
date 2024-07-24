from pydantic import BaseModel


class CreateAndUpdateHadith(BaseModel):
    hadith_arab: str
    hadith_melayu: str
    explanation: str
    evaluation_id: int
