from pydantic import BaseModel


class CreateHadithAssesment(BaseModel):
    created_by: int
    updated_by: int
    user_id: int
    hadith_id: int
    evaluation_id: int


class UpdateHadithAssesment(BaseModel):
    created_by: int
    updated_by: int
    user_id: int
    hadith_id: int
    evaluation_id: int
