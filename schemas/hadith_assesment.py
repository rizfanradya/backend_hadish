from pydantic import BaseModel


class CreateHadithAssesment(BaseModel):
    hadith_id: int
    evaluation_id: int


class UpdateHadithAssesment(BaseModel):
    evaluation_id: int
