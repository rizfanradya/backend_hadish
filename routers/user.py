from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import CreateUser, UpdateUser
from database import get_db
from typing import Optional
from cruds.user import create_user, get_all_user, get_user_by_id, get_login, update_user, delete_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/user')
def create_new_user(user_info: CreateUser, session: Session = Depends(get_db)):
    return create_user(session, user_info)


@router.post("/token")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return get_login(session, form_data)


@router.get('/user')
def get_user(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_all_user(session, limit, offset, search)


@router.get("/user/{id}")
def get_user_byid(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_user_by_id(session, id)


@router.put("/user/{id}", response_model=UpdateUser)
def update_user_info(id: int, info_update: UpdateUser, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return update_user(session, id, info_update)


@router.delete("/user/{id}")
def delete_user_info(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return delete_user(session, id)
