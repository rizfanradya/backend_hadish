from sqlalchemy.orm import Session
from schemas.hadith_assesment import CreateHadithAssesment, UpdateHadithAssesment
from models.hadithAssesment import HadithAssesment
from models.typehadith import TypeHadith
from typing import Optional
from sqlalchemy import or_
from fastapi import HTTPException
from cruds.user import get_user_by_id
from cruds.hadith import GetHadithById


def CreateHadithAssesmentInfo(session: Session, hadith_assesment_info: CreateHadithAssesment, token_info):
    hadith_assesment = session.query(HadithAssesment).where(
        HadithAssesment.user_id == token_info.id, HadithAssesment.hadith_id == hadith_assesment_info.hadith_id).first()

    if hadith_assesment:
        raise HTTPException(
            status_code=404, detail=f'The user assessment with ID "{token_info.id}" of the hadith with ID "{hadith_assesment_info.hadith_id}" is already exists'
        )

    try:
        new_hadith_assesment = HadithAssesment(**hadith_assesment_info.dict())
        new_hadith_assesment.created_by = token_info.id
        new_hadith_assesment.user_id = token_info.id

        session.add(new_hadith_assesment)
        session.commit()
        session.refresh(new_hadith_assesment)
        return new_hadith_assesment
    except Exception as error:
        raise HTTPException(
            status_code=404, detail=f'evaluation id "{hadith_assesment_info.evaluation_id}" or hadith id "{hadith_assesment_info.hadith_id}" not found')


def GetAllHadithAssesment(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_hadith_assesment = session.query(HadithAssesment)

    if search:
        all_hadith_assesment = all_hadith_assesment.filter(or_(*[getattr(HadithAssesment, column).ilike(
            f"%{search}%"
        ) for column in HadithAssesment
            .__table__.columns.keys()]))  # type: ignore

    total_data = all_hadith_assesment.count()
    all_hadith_assesment = all_hadith_assesment.offset(
        offset).limit(limit).all()  # type: ignore

    for hadith_assesment in all_hadith_assesment:
        hadith_assesment.evaluation_name = session.query(TypeHadith).get(
            hadith_assesment.evaluation_id).type if session.query(TypeHadith).get(hadith_assesment.evaluation_id) else None  # type: ignore
        hadith_assesment.user_info = get_user_by_id(
            session, hadith_assesment.user_id, error_handling=False)  # type: ignore
        hadith_assesment.hadith_info = GetHadithById(
            session, hadith_assesment.hadith_id, False, False)  # type: ignore

    return {
        "total_data": total_data,
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
        hadith_assesment_info.evaluation_name = session.query(TypeHadith).get(
            hadith_assesment_info.evaluation_id).type if session.query(TypeHadith).get(hadith_assesment_info.evaluation_id) else None  # type: ignore
        hadith_assesment_info.user_info = get_user_by_id(
            session, hadith_assesment_info.user_id, error_handling=False)  # type: ignore
        hadith_assesment_info.hadith_info = GetHadithById(
            session, hadith_assesment_info.hadith_id, error_handling=False)  # type: ignore

    return hadith_assesment_info


def GetAllHadithAssesmentByHadithId(session: Session, hadith_id: int):
    hadith_assesment_info = session.query(
        HadithAssesment).where(HadithAssesment.hadith_id == hadith_id).all()

    for hadith_assesment in hadith_assesment_info:
        hadith_assesment.evaluation_name = session.query(TypeHadith).get(
            hadith_assesment.evaluation_id).type if session.query(TypeHadith).get(hadith_assesment.evaluation_id) else None  # type: ignore
        hadith_assesment.username = get_user_by_id(
            session, hadith_assesment.user_id, error_handling=False).username  # type: ignore

    return hadith_assesment_info


def GetHadithAssesmentByHadith(session: Session, hadith_id: str, limit: int, offset: int, search: Optional[str] = None):
    hadith_assesment_info = session.query(
        HadithAssesment).where(HadithAssesment.hadith_id == hadith_id)

    if search:
        hadith_assesment_info = hadith_assesment_info.filter(or_(*[getattr(HadithAssesment, column).ilike(
            f"%{search}%"
        ) for column in HadithAssesment
            .__table__.columns.keys()]))  # type: ignore

    total_data = hadith_assesment_info.count()
    hadith_assesment_info = hadith_assesment_info.offset(
        offset).limit(limit).all()  # type: ignore

    for hadith_assesment in hadith_assesment_info:
        hadith_assesment.evaluation_name = session.query(TypeHadith).get(
            hadith_assesment.evaluation_id).type if session.query(TypeHadith).get(hadith_assesment.evaluation_id) else None  # type: ignore
        hadith_assesment.user_info = get_user_by_id(
            session, hadith_assesment.user_id, error_handling=False)  # type: ignore
        hadith_assesment.hadith_info = GetHadithById(
            session, hadith_assesment.hadith_id, False, False)  # type: ignore

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": hadith_assesment_info
    }


def GetHadithAssesmentByUser(session: Session, user_id: int, limit: int, offset: int, search: Optional[str] = None):
    hadith_assesment_info = session.query(
        HadithAssesment).where(HadithAssesment.user_id == user_id)

    if search:
        hadith_assesment_info = hadith_assesment_info.filter(or_(*[getattr(HadithAssesment, column).ilike(
            f"%{search}%"
        ) for column in HadithAssesment
            .__table__.columns.keys()]))  # type: ignore

    total_data = hadith_assesment_info.count()
    hadith_assesment_info = hadith_assesment_info.offset(
        offset).limit(limit).all()  # type: ignore

    for hadith_assesment in hadith_assesment_info:
        hadith_assesment.evaluation_name = session.query(TypeHadith).get(
            hadith_assesment.evaluation_id).type if session.query(TypeHadith).get(hadith_assesment.evaluation_id) else None  # type: ignore
        hadith_assesment.user_info = get_user_by_id(
            session, hadith_assesment.user_id, error_handling=False)  # type: ignore
        hadith_assesment.hadith_info = GetHadithById(
            session, hadith_assesment.hadith_id, error_handling=False)  # type: ignore

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": hadith_assesment_info
    }


def UpdateHadithAssesmentInfo(session: Session, id: int, info_update: UpdateHadithAssesment, token_info):
    hadith_assesment_info = GetHadithAssesmentById(session, id, False)

    try:
        hadith_assesment_info.updated_by = token_info.id  # type: ignore
        for attr, value in info_update.__dict__.items():
            setattr(hadith_assesment_info, attr, value)
        session.commit()
        session.refresh(hadith_assesment_info)
        return hadith_assesment_info.__dict__
    except Exception as error:
        raise HTTPException(
            status_code=404, detail=f'evaluation id "{info_update.evaluation_id}" not found')


def DeleteHadithAssesment(session: Session, id: int):
    hadith_assesment_info = GetHadithAssesmentById(session, id, False)
    session.delete(hadith_assesment_info)
    session.commit()
    return f"Hadith assesment id '{id}' deleted success"
