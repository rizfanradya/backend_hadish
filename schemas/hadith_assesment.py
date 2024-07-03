from pydantic import BaseModel


class CreateHadithAssesment(BaseModel):
    created_by: int
    user_id: int
    hadith_id: int
    evaluation_id: int


class UpdateHadithAssesment(BaseModel):
    updated_by: int
    evaluation_id: int
