from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import CreateAndUpdateUser
from database import get_db
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/user')
def create_new_user(user_info: CreateAndUpdateUser, session: Session = Depends(get_db)):
    return 'ok'


@router.post("/token")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return 'ok'


@router.get('/user')
def get_user(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return 'ok'


@router.get("/user/{id}")
def get_user_byid(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return 'ok'


@router.put("/user/{id}", response_model=CreateAndUpdateUser)
def update_user_info(id: int, info_update: CreateAndUpdateUser, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return 'ok'


@router.delete("/user/{id}")
def delete_user(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return 'ok'
