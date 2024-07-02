from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from fastapi import HTTPException
from models.hadith import Hadith
from models.typehadith import TypeHadith
from utils import format_datetime
from typing import Optional
from sqlalchemy import or_
from .typehadith import GetTypeHadithById
from models.user import UserInfo


def CreateHadith(session: Session, hadith_info: CreateAndUpdateHadith):
    if hadith_info.type_hadith:
        GetTypeHadithById(session, hadith_info.type_hadith, False)
    new_hadith_info = Hadith(**hadith_info.dict())
    session.add(new_hadith_info)
    session.commit()
    session.refresh(new_hadith_info)
    return new_hadith_info


def GetAllHadith(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_hadith = session.query(Hadith)
    type_hadith_info = session.query(TypeHadith).all()
    type_hadith_mapping = {
        type_hadith.id: type_hadith for type_hadith in type_hadith_info}

    if search:
        all_hadith = all_hadith.filter(or_(*[getattr(Hadith, column).ilike(
            f"%{search}%"
        ) for column in Hadith.__table__.columns.keys()]))  # type: ignore

    all_hadith = all_hadith.offset(offset).limit(limit).all()  # type: ignore

    for hadith in all_hadith:
        hadith.type_hadith_name = type_hadith_mapping.get(hadith.type_hadith).type if type_hadith_mapping.get(  # type: ignore
            hadith.type_hadith) else None
        hadith.created_by_name = session.query(UserInfo).get(
            hadith.created_by).username if session.query(UserInfo).get(hadith.created_by) else None
        hadith.updated_by_name = session.query(UserInfo).get(
            hadith.updated_by).username if session.query(UserInfo).get(hadith.updated_by) else None
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
        hadith_info.type_hadith_name = GetTypeHadithById(
            session, hadith_info.type_hadith, False, False)
        hadith_info.created_by_name = session.query(UserInfo).get(
            hadith_info.created_by).username if session.query(UserInfo).get(hadith_info.created_by) else None
        hadith_info.updated_by_name = session.query(UserInfo).get(
            hadith_info.updated_by).username if session.query(UserInfo).get(hadith_info.updated_by) else None
        hadith_info.created_at = format_datetime(hadith_info.created_at)
        hadith_info.updated_at = format_datetime(hadith_info.updated_at)

    return hadith_info


def UpdateHadith(session: Session, id: int, info_update: CreateAndUpdateHadith):
    if info_update.type_hadith:
        GetTypeHadithById(session, info_update.type_hadith, False)
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
