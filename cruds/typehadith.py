from sqlalchemy.orm import Session
from schemas.typehadith import CreateAndUpdateTypeHadith
from fastapi import HTTPException
from models.typehadith import TypeHadith
from typing import Optional
from sqlalchemy import or_


def CreateTypeHadith(session: Session, type_hadith_info: CreateAndUpdateTypeHadith, token_info):
    try:
        new_type_hadith_info = TypeHadith(**type_hadith_info.dict())
        new_type_hadith_info.created_by = token_info.id

        session.add(new_type_hadith_info)
        session.commit()
        session.refresh(new_type_hadith_info)
        return new_type_hadith_info
    except Exception as error:
        raise HTTPException(
            status_code=404, detail=f'Type hadish "{type_hadith_info.type}" is already exist')


def GetAllTypeHadith(session: Session, limit: int, offset: int, search: Optional[str] = None):
    all_type_hadith = session.query(TypeHadith)

    if search:
        all_type_hadith = all_type_hadith.filter(or_(*[getattr(TypeHadith, column).ilike(
            f"%{search}%"
        ) for column in TypeHadith.__table__.columns.keys()]))  # type: ignore

    total_data = all_type_hadith.count()
    all_type_hadith = all_type_hadith.offset(
        offset).limit(limit).all()  # type: ignore

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_type_hadith
    }


def GetTypeHadithById(session: Session, id: int, error_handling: bool = True):
    type_hadith_info = session.query(TypeHadith).get(id)

    if type_hadith_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"Type Hadith id {id} not found")
        else:
            return

    return type_hadith_info


def UpdateTypeHadith(session: Session, id: int, info_update: CreateAndUpdateTypeHadith, token_info):
    type_hadith_info = GetTypeHadithById(session, id)
    type_hadith_info.updated_by = token_info.id  # type: ignore

    for attr, value in info_update.__dict__.items():
        setattr(type_hadith_info, attr, value)
    session.commit()
    session.refresh(type_hadith_info)
    return type_hadith_info.__dict__


def DeleteTypeHadith(session: Session, id: int):
    type_hadith_info = GetTypeHadithById(session, id)
    session.delete(type_hadith_info)
    session.commit()
    return f"Hadith id {id} deleted success"
