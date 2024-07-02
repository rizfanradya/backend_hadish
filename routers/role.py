from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from schemas.role import CreateAndUpdateRole
from sqlalchemy.orm import Session
from database import get_db
from cruds.role import CreateRole, GetAllRole, GetRoleById, GetRoleByRole, UpdateRole, DeleteRole
from typing import Optional
from cruds.user import TokenAuthorization

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/role')
def create_role(role_info: CreateAndUpdateRole, session: Session = Depends(get_db)):
    return CreateRole(session, role_info)


@router.get('/role')
def get_role(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetAllRole(session, limit, offset, search)


@router.get("/role/{id}")
def get_role_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetRoleById(session, id)


@router.get("/role/name/{role}")
def get_role_by_role(role: str, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetRoleByRole(session, role)


@router.put("/role/{id}")
def update_role_info(id: int, info_update: CreateAndUpdateRole, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return UpdateRole(session, id, info_update)


@router.delete("/role/{id}")
def delete_role(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return DeleteRole(session, id)
