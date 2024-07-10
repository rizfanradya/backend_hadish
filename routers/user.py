from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import CreateUser, UpdateUser
from database import get_db
from typing import Optional
from cruds.user import create_user, get_all_user, get_user_by_id, get_login, update_user, delete_user, GetUserByUsername, TokenAuthorization, RefreshToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/user')
def create_new_user(user_info: CreateUser, session: Session = Depends(get_db)):
    return create_user(session, user_info)


@router.post("/token")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return get_login(session, form_data)


@router.get("/refresh_token")
async def refresh_token(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)):
    TokenAuthorization(session, token)
    return RefreshToken(session, token)


@router.get('/user')
def get_user(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return get_all_user(session, limit, offset, search)


@router.get("/user/{id}")
def get_user_byid(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return get_user_by_id(session, id)


@router.get("/user/username/{username}")
def get_user_by_username(username: str, session: Session = Depends(get_db)):
    return GetUserByUsername(session, username)


@router.put("/user/{id}", response_model=UpdateUser)
def update_user_info(id: int, info_update: UpdateUser, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return update_user(session, id, info_update, token_info)


@router.delete("/user/{id}")
def delete_user_info(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return delete_user(session, id)
