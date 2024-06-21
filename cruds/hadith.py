from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from fastapi import HTTPException
from models.hadith import Hadith
from utils import format_datetime
from typing import Optional
from sqlalchemy import or_
from .user import get_user_by_id


def CreateHadith(session: Session, hadith_info: CreateAndUpdateHadith):
    new_hadith_info = Hadith(**hadith_info.dict())
    session.add(new_hadith_info)
    session.commit()
    session.refresh(new_hadith_info)
    return new_hadith_info


def GetAllHadith(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_hadith = session.query(Hadith)

    if search:
        all_hadith = all_hadith.filter(or_(*[getattr(Hadith, column).ilike(
            f"%{search}%"
        ) for column in Hadith.__table__.columns.keys()]))  # type: ignore

    all_hadith = all_hadith.offset(offset).limit(limit).all()  # type: ignore

    for hadith in all_hadith:
        hadith.created_by = get_user_by_id(
            session, hadith.created_by, False, False).username  # type: ignore
        hadith.updated_by = get_user_by_id(
            session, hadith.updated_by, False, False).username  # type: ignore
        hadith.created_at = format_datetime(hadith.created_at)
        hadith.updated_at = format_datetime(hadith.updated_at)

    return {
        "total_data": len(all_hadith),
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_hadith
    }


def GetHadithById(session: Session, id: int, format: bool = True):
    hadith_info = session.query(Hadith).get(id)

    if hadith_info is None:
        raise HTTPException(
            status_code=404, detail=f"Hadith id {id} not found")

    if format:
        hadith_info.created_by = get_user_by_id(
            session, hadith_info.created_by, False, False).username  # type: ignore
        hadith_info.updated_by = get_user_by_id(
            session, hadith_info.updated_by, False, False).username  # type: ignore
        hadith_info.created_at = format_datetime(hadith_info.created_at)
        hadith_info.updated_at = format_datetime(hadith_info.updated_at)

    return hadith_info


def UpdateHadith(session: Session, id: int, info_update: CreateAndUpdateHadith):
    hadith_info = GetHadithById(session, id, False)
    for attr, value in info_update.__dict__.items():
        setattr(hadith_info, attr, value)
    session.commit()
    session.refresh(hadith_info)
    return hadith_info.__dict__


def DeleteHadith(session: Session, id: int):
    hadith_info = GetHadithById(session, id, False)
    session.delete(hadith_info)
    session.commit()
    return f"Hadith id {id} deleted success"
