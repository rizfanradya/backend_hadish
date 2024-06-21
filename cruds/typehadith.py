from sqlalchemy.orm import Session
from schemas.typehadith import CreateAndUpdateTypeHadith
from fastapi import HTTPException
from models.typehadith import TypeHadith
from utils import format_datetime
from typing import Optional
from sqlalchemy import or_
from .user import get_user_by_id


def CreateTypeHadith(session: Session, type_hadith_info: CreateAndUpdateTypeHadith):
    new_type_hadith_info = TypeHadith(**type_hadith_info.dict())
    session.add(new_type_hadith_info)
    session.commit()
    session.refresh(new_type_hadith_info)
    return new_type_hadith_info


def GetAllTypeHadith(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_type_hadith = session.query(TypeHadith)

    if search:
        all_type_hadith = all_type_hadith.filter(or_(*[getattr(TypeHadith, column).ilike(
            f"%{search}%"
        ) for column in TypeHadith.__table__.columns.keys()]))  # type: ignore

    all_type_hadith = all_type_hadith.offset(
        offset).limit(limit).all()  # type: ignore

    for type_hadith in all_type_hadith:
        type_hadith.created_by = get_user_by_id(
            session, type_hadith.created_by, False, False).username  # type: ignore
        type_hadith.updated_by = get_user_by_id(
            session, type_hadith.updated_by, False, False).username  # type: ignore
        type_hadith.created_at = format_datetime(type_hadith.created_at)
        type_hadith.updated_at = format_datetime(type_hadith.updated_at)

    return {
        "total_data": len(all_type_hadith),
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_type_hadith
    }


def GetTypeHadithById(session: Session, id: int, format: bool = True):
    type_hadith_info = session.query(TypeHadith).get(id)

    if type_hadith_info is None:
        raise HTTPException(
            status_code=404, detail=f"Type Hadith id {id} not found")

    if format:
        type_hadith_info.created_by = get_user_by_id(
            session, type_hadith_info.created_by, False, False).username  # type: ignore
        type_hadith_info.updated_by = get_user_by_id(
            session, type_hadith_info.updated_by, False, False).username  # type: ignore
        type_hadith_info.created_at = format_datetime(
            type_hadith_info.created_at)
        type_hadith_info.updated_at = format_datetime(
            type_hadith_info.updated_at)

    return type_hadith_info


def UpdateTypeHadith(session: Session, id: int, info_update: CreateAndUpdateTypeHadith):
    type_hadith_info = GetTypeHadithById(session, id, False)
    for attr, value in info_update.__dict__.items():
        setattr(type_hadith_info, attr, value)
    session.commit()
    session.refresh(type_hadith_info)
    return type_hadith_info.__dict__


def DeleteTypeHadith(session: Session, id: int):
    type_hadith_info = GetTypeHadithById(session, id, False)
    session.delete(type_hadith_info)
    session.commit()
    return f"Hadith id {id} deleted success"
