from sqlalchemy.orm import Session
from schemas.hadith_assesment import CreateHadithAssesment, UpdateHadithAssesment
from models.hadithAssesment import HadithAssesment
from typing import Optional
from sqlalchemy import or_
from models.user import UserInfo
from utils import format_datetime
from fastapi import HTTPException


def CreateHadithAssesmentInfo(session: Session, hadith_assesment_info: CreateHadithAssesment):
    new_hadith_assesment = HadithAssesment(**hadith_assesment_info.dict())
    session.add(new_hadith_assesment)
    session.commit()
    session.refresh(new_hadith_assesment)
    return new_hadith_assesment


def GetAllHadithAssesment(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_hadith_assesment = session.query(HadithAssesment)

    if search:
        all_hadith_assesment = all_hadith_assesment.filter(or_(*[getattr(HadithAssesment, column).ilike(
            f"%{search}%"
        ) for column in HadithAssesment
            .__table__.columns.keys()]))  # type: ignore

    all_hadith_assesment = all_hadith_assesment.offset(
        offset).limit(limit).all()  # type: ignore

    for hadith_assesment in all_hadith_assesment:
        hadith_assesment.created_by_name = session.query(UserInfo).get(
            hadith_assesment.created_by).username if session.query(UserInfo).get(hadith_assesment.created_by) else None
        hadith_assesment.updated_by_name = session.query(UserInfo).get(
            hadith_assesment.updated_by).username if session.query(UserInfo).get(hadith_assesment.updated_by) else None
        hadith_assesment.created_at = format_datetime(
            hadith_assesment.created_at)
        hadith_assesment.updated_at = format_datetime(
            hadith_assesment.updated_at)

    return {
        "total_data": len(all_hadith_assesment),
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_hadith_assesment
    }


def GetHadithAssesmentById(session: Session, id: int, format: bool = True, error_handling: bool = True):
    hadith_assesment_info = session.query(HadithAssesment).get(id)

    if hadith_assesment_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"Hadith assesment id '{id}' not found")
        else:
            return

    if format:
        hadith_assesment_info.created_by_name = session.query(UserInfo).get(
            hadith_assesment_info.created_by).username if session.query(UserInfo).get(hadith_assesment_info.created_by) else None
        hadith_assesment_info.updated_by_name = session.query(UserInfo).get(
            hadith_assesment_info.updated_by).username if session.query(UserInfo).get(hadith_assesment_info.updated_by) else None
        hadith_assesment_info.created_at = format_datetime(
            hadith_assesment_info.created_at)
        hadith_assesment_info.updated_at = format_datetime(
            hadith_assesment_info.updated_at)

    return hadith_assesment_info


def GetHadithAssesmentByHadith(session: Session, hadith: str, format: bool = True, error_handling: bool = True):
    hadith_assesment_info = session.query(
        HadithAssesment).where(HadithAssesment.hadith == hadith).first()

    if hadith_assesment_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"Hadith assesment '{hadith}' not found")
        else:
            return

    if format:
        hadith_assesment_info.created_by_name = session.query(UserInfo).get(
            hadith_assesment_info.created_by).username if session.query(UserInfo).get(hadith_assesment_info.created_by) else None
        hadith_assesment_info.updated_by_name = session.query(UserInfo).get(
            hadith_assesment_info.updated_by).username if session.query(UserInfo).get(hadith_assesment_info.updated_by) else None
        hadith_assesment_info.created_at = format_datetime(
            hadith_assesment_info.created_at)
        hadith_assesment_info.updated_at = format_datetime(
            hadith_assesment_info.updated_at)

    return hadith_assesment_info


def UpdateHadithAssesmentInfo(session: Session, id: int, info_update: UpdateHadithAssesment):
    hadith_assesment_info = GetHadithAssesmentById(session, id, False)
    for attr, value in info_update.__dict__.items():
        setattr(hadith_assesment_info, attr, value)
    session.commit()
    session.refresh(hadith_assesment_info)
    return hadith_assesment_info.__dict__


def DeleteHadithAssesment(session: Session, id: int):
    hadith_assesment_info = GetHadithAssesmentById(session, id, False)
    session.delete(hadith_assesment_info)
    session.commit()
    return f"Hadith assesment id '{id}' deleted success"