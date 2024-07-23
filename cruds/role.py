from sqlalchemy.orm import Session
from schemas.role import CreateAndUpdateRole
from fastapi import HTTPException
from models.role import Role
from typing import Optional
from sqlalchemy import or_


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

    total_data = all_role.count()
    all_role = all_role.offset(offset).limit(limit).all()  # type: ignore

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_role
    }


def GetRoleById(session: Session, id: int):
    role_info = session.query(Role).get(id)

    if role_info is None:
        raise HTTPException(
            status_code=404, detail=f"Role id {id} not found")

    return role_info


def GetRoleByRole(session: Session, role: str):
    role_info = session.query(Role).where(Role.role == role).first()

    if role_info is None:
        raise HTTPException(
            status_code=404, detail=f"Role '{role}' not found")

    return role_info


def UpdateRole(session: Session, id: int, info_update: CreateAndUpdateRole, token_info):
    role_info = GetRoleById(session, id)

    try:
        info_update.role = info_update.role.upper()
        role_info.updated_by = token_info.id

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
