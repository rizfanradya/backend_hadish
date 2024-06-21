from numpy import info
from sqlalchemy.orm import Session
from schemas.role import CreateAndUpdateRole
from fastapi import HTTPException
from models.role import Role
from utils import format_datetime
from typing import Optional
from sqlalchemy import or_
from .user import get_user_by_id


def CreateRole(session: Session, role_info: CreateAndUpdateRole):
    try:
        new_role_info = Role(**role_info.dict())
        new_role_info.role = new_role_info.role.upper()

        session.add(new_role_info)
        session.commit()
        session.refresh(new_role_info)
        return new_role_info

    except Exception as error:
        raise HTTPException(
            status_code=404, detail=f'Role "{role_info.role}" is already exist')


def GetAllRole(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_role = session.query(Role)

    if search:
        all_role = all_role.filter(or_(*[getattr(Role, column).ilike(
            f"%{search}%"
        ) for column in Role.__table__.columns.keys()]))  # type: ignore

    all_role = all_role.offset(offset).limit(limit).all()  # type: ignore

    for role in all_role:
        role.created_by = get_user_by_id(
            session, role.created_by, False, False)
        role.updated_by = get_user_by_id(
            session, role.updated_by, False, False)
        role.created_at = format_datetime(role.created_at)
        role.updated_at = format_datetime(role.updated_at)

    return {
        "total_data": len(all_role),
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_role
    }


def GetRoleById(session: Session, id: int, format: bool = True):
    role_info = session.query(Role).get(id)

    if role_info is None:
        raise HTTPException(
            status_code=404, detail=f"Role id {id} not found")

    if format:
        role_info.created_by = get_user_by_id(
            session, role_info.created_by, False, False)
        role_info.updated_by = get_user_by_id(
            session, role_info.updated_by, False, False)
        role_info.created_at = format_datetime(role_info.created_at)
        role_info.updated_at = format_datetime(role_info.updated_at)

    return role_info


def UpdateRole(session: Session, id: int, info_update: CreateAndUpdateRole):
    role_info = GetRoleById(session, id, False)

    try:
        info_update.role = info_update.role.upper()
        for attr, value in info_update.__dict__.items():
            setattr(role_info, attr, value)

        session.commit()
        session.refresh(role_info)
        return role_info.__dict__
    except Exception as error:
        print(error)
        raise HTTPException(
            status_code=404, detail=f'Role "{info_update.role}" is already exist')


def DeleteRole(session: Session, id: int):
    role_info = GetRoleById(session, id)
    session.delete(role_info)
    session.commit()
    return f"Role id {id} deleted success"
