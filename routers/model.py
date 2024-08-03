from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from typing import Optional
from cruds.user import TokenAuthorization
from cruds.model import CreateModel, GetAllModel, GetModelById, UpdateModel, DeleteModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/model')
def create_model(name: str, status: bool, file: UploadFile = File(...), session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return CreateModel(session, name, status, file)


@router.get('/model')
def get_model(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetAllModel(session, limit, offset, search)


@router.get("/model/{id}")
def get_model_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetModelById(session, id)


@router.put("/model/{id}")
def update_model_info(id: int, name: str, status: bool, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return UpdateModel(session, id, name, status)


@router.delete("/model/{id}")
def delete_model(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return DeleteModel(session, id)
