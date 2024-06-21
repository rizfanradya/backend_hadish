from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from database import get_db
from typing import Optional
from cruds.hadith import CreateHadith, GetAllHadith, GetHadithById, UpdateHadith, DeleteHadith

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/hadith')
def create_new_hadith(hadith_info: CreateAndUpdateHadith, session: Session = Depends(get_db)):
    return CreateHadith(session, hadith_info)


@router.get('/hadith')
def get_hadith(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return GetAllHadith(session, limit, offset, search)


@router.get("/hadith/{id}")
def get_hadith_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return GetHadithById(session, id)


@router.put("/hadith/{id}", response_model=CreateAndUpdateHadith)
def update_hadith(id: int, info_update: CreateAndUpdateHadith, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return UpdateHadith(session, id, info_update)


@router.delete("/hadith/{id}")
def delete_hadith(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return DeleteHadith(session, id)
