from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from fastapi import HTTPException
from models.hadith import Hadith
from models.hadithAssesment import HadithAssesment
from utils import format_datetime
from typing import Optional
from sqlalchemy import or_
from models.user import UserInfo
from fastapi import File, UploadFile
import pandas as pd
from io import BytesIO
from fastapi import File
from starlette.responses import FileResponse
import os
from sqlalchemy import func


def CreateHadith(session: Session, hadith_info: CreateAndUpdateHadith, token_info):
    new_hadith_info = Hadith(**hadith_info.dict())
    new_hadith_info.created_by = token_info.id

    session.add(new_hadith_info)
    session.commit()
    session.refresh(new_hadith_info)
    return new_hadith_info


async def UploadFileHadith(session: Session, token_info, file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):  # type: ignore
        raise HTTPException(
            status_code=404, detail="Invalid file format. Only .xlsx files are allowed.")

    try:
        df = pd.read_excel(file.file)
    except Exception as error:
        try:
            file.file.seek(0)
            excel_data = file.file.read()
            file_bytes = BytesIO(excel_data)
            df = pd.read_excel(file_bytes)
        except:
            raise HTTPException(
                status_code=404, detail="Could not read the Excel file.")

    try:
        df = df.fillna('')
        hadith_entries = []
        for _, row in df.iterrows():
            hadith_entry = Hadith(
                hadith_arab=row['hadish_arab'],
                hadith_melayu=row['hadish_melayu'],
                explanation=row['keterangan'],
                created_by=token_info.id,
                updated_by=token_info.id
            )  # type: ignore
            hadith_entries.append(hadith_entry)

        session.bulk_save_objects(hadith_entries)
        session.commit()
    except Exception as error:
        raise HTTPException(status_code=404, detail='Invalid Excel format')

    return hadith_entries


def DownloadExcel():
    file_path = "/project/backend_hadish/uploads/format.xlsx"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, filename="format.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


def GetAllHadith(session: Session, limit: int, offset: int, filter_by, amount_of_appraisers, search: Optional[str] = None):
    from cruds.hadith_assesment import GetAllHadithAssesmentByHadithId

    if filter_by == 'all':
        all_hadith = session.query(Hadith)
    else:
        all_hadith = session.query(Hadith).filter(HadithAssesment.hadith_id == Hadith.id).group_by(
            Hadith.id).having(func.count(HadithAssesment.id) == amount_of_appraisers)

    if search:
        all_hadith = all_hadith.filter(or_(*[getattr(Hadith, column).ilike(
            f"%{search}%"
        ) for column in Hadith.__table__.columns.keys()]))  # type: ignore

    total_data = all_hadith.count()
    all_hadith = all_hadith.offset(offset).limit(limit).all()

    for hadith in all_hadith:
        hadith.assesed = GetAllHadithAssesmentByHadithId(
            session, hadith.id)  # type: ignore
        hadith.created_by_name = session.query(UserInfo).get(
            hadith.created_by).username if session.query(UserInfo).get(hadith.created_by) else None  # type: ignore
        hadith.updated_by_name = session.query(UserInfo).get(
            hadith.updated_by).username if session.query(UserInfo).get(hadith.updated_by) else None  # type: ignore
        hadith.created_at = format_datetime(  # type: ignore
            hadith.created_at)
        hadith.updated_at = format_datetime(  # type: ignore
            hadith.updated_at)

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_hadith
    }


def GetAllHadithEvaluate(session: Session, limit: int, offset: int, user_id, search: Optional[str] = None):
    all_hadith = session.query(Hadith).filter(~Hadith.id.in_(session.query(
        HadithAssesment.hadith_id).filter(HadithAssesment.user_id == user_id)))

    if search:
        all_hadith = all_hadith.filter(or_(*[getattr(Hadith, column).ilike(
            f"%{search}%"
        ) for column in Hadith.__table__.columns.keys()]))  # type: ignore

    total_data = all_hadith.count()
    all_hadith = all_hadith.offset(offset).limit(limit).all()

    for hadith in all_hadith:
        hadith.created_by_name = session.query(UserInfo).get(
            hadith.created_by).username if session.query(UserInfo).get(hadith.created_by) else None  # type: ignore
        hadith.updated_by_name = session.query(UserInfo).get(
            hadith.updated_by).username if session.query(UserInfo).get(hadith.updated_by) else None  # type: ignore
        hadith.created_at = format_datetime(  # type: ignore
            hadith.created_at)
        hadith.updated_at = format_datetime(  # type: ignore
            hadith.updated_at)

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_hadith
    }


def GetHadithById(session: Session, id: int, format: bool = True, error_handling: bool = True):
    hadith_info = session.query(Hadith).get(id)

    if hadith_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"Hadith id {id} not found")
        else:
            return

    if format:
        hadith_info.created_by_name = session.query(UserInfo).get(
            hadith_info.created_by).username if session.query(UserInfo).get(hadith_info.created_by) else None  # type: ignore
        hadith_info.updated_by_name = session.query(UserInfo).get(
            hadith_info.updated_by).username if session.query(UserInfo).get(hadith_info.updated_by) else None  # type: ignore
        hadith_info.created_at = format_datetime(hadith_info.created_at)
        hadith_info.updated_at = format_datetime(hadith_info.updated_at)

    return hadith_info


def UpdateHadith(session: Session, id: int, info_update: CreateAndUpdateHadith, token_info):
    hadith_info = GetHadithById(session, id, False)

    hadith_info.updated_by = token_info.id  # type: ignore
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
