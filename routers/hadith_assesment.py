from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.hadith_assesment import CreateHadithAssesment, UpdateHadithAssesment
from database import get_db
from typing import Optional
from cruds.hadith_assesment import CreateHadithAssesmentInfo, GetAllHadithAssesment, GetHadithAssesmentByHadith, GetHadithAssesmentById, GetHadithAssesmentByUser, UpdateHadithAssesmentInfo, DeleteHadithAssesment
from cruds.user import TokenAuthorization

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/hadith_assesment')
def create_new_hadith_assesment(hadith_assesment_info: CreateHadithAssesment, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return CreateHadithAssesmentInfo(session, hadith_assesment_info, token_info)


@router.get('/hadith_assesment')
def get_hadith_assesment(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetAllHadithAssesment(session, limit, offset, search)


@router.get("/hadith_assesment/{id}")
def get_hadith_assesment_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetHadithAssesmentById(session, id)


@router.get("/hadith_assesment/hadith_id/{hadith_id}")
def get_hadith_assesment_by_hadith_id(hadith_id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetHadithAssesmentByHadith(session, hadith_id)


@router.get("/hadith_assesment/user_id/{user_id}")
def get_hadith_assesment_by_user_id(user_id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetHadithAssesmentByUser(session, user_id)


@router.put("/hadith_assesment/{id}", response_model=UpdateHadithAssesment)
def update_hadith_assesment(id: int, info_update: UpdateHadithAssesment, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return UpdateHadithAssesmentInfo(session, id, info_update, token_info)


@router.delete("/hadith_assesment/{id}")
def delete_hadith_assesment(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return DeleteHadithAssesment(session, id)
