from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.typehadith import CreateAndUpdateTypeHadith
from database import get_db
from typing import Optional
from cruds.typehadith import CreateTypeHadith, GetAllTypeHadith, GetTypeHadithById, UpdateTypeHadith, DeleteTypeHadith

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/type_hadith')
def create_new_type_hadith(type_hadith_info: CreateAndUpdateTypeHadith, session: Session = Depends(get_db)):
    return CreateTypeHadith(session, type_hadith_info)


@router.get('/type_hadith')
def get_type_hadith(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return GetAllTypeHadith(session, limit, offset, search)


@router.get("/type_hadith/{id}")
def get_type_hadith_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return GetTypeHadithById(session, id)


@router.put("/type_hadith/{id}", response_model=CreateAndUpdateTypeHadith)
def update_type_hadith(id: int, info_update: CreateAndUpdateTypeHadith, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return UpdateTypeHadith(session, id, info_update)


@router.delete("/type_hadith/{id}")
def delete_type_hadith(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return DeleteTypeHadith(session, id)
