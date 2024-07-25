from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from schemas.hadith_assesment import UpdateHadithAssesment, CreateHadithAssesment
from fastapi import HTTPException
from models.hadith import Hadith
from models.hadithAssesment import HadithAssesment
from typing import Optional
from sqlalchemy import or_
from fastapi import File, UploadFile
import pandas as pd
from io import BytesIO
from fastapi import File
from starlette.responses import FileResponse
import os


def CreateHadith(session: Session, hadith_info: CreateAndUpdateHadith, token_info):
    from cruds.hadith_assesment import CreateHadithAssesmentInfo

    evaluation_id = hadith_info.evaluation_id
    hadith_info_dict = hadith_info.dict()
    del hadith_info_dict['evaluation_id']

    new_hadith_info = Hadith(**hadith_info_dict)
    new_hadith_info.created_by = token_info.id

    session.add(new_hadith_info)
    session.flush()

    CreateHadithAssesmentInfo(
        session,
        CreateHadithAssesment(
            hadith_id=new_hadith_info.id,  # type: ignore
            evaluation_id=evaluation_id,
        ),
        token_info)

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


def DownloadTemplate():
    file_path = "/project/backend_hadish/uploads/format.xlsx"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, filename="format.xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


def DownloadHadith(session: Session):
    return


def GetAllHadith(session: Session, limit: int, offset: int, search: Optional[str] = None):
    from cruds.hadith_assesment import GetAllHadithAssesmentByHadithId

    all_hadith = session.query(Hadith)

    if search:
        all_hadith = all_hadith.filter(or_(*[getattr(Hadith, column).ilike(
            f"%{search}%"
        ) for column in Hadith.__table__.columns.keys()]))  # type: ignore

    total_data = all_hadith.count()
    all_hadith = all_hadith.offset(offset).limit(limit).all()

    for hadith in all_hadith:
        hadith.assesed = GetAllHadithAssesmentByHadithId(
            session, hadith.id)  # type: ignore

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

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_hadith
    }


def GetHadithById(session: Session, id: int, error_handling: bool = True):
    hadith_info = session.query(Hadith).get(id)

    if hadith_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"Hadith id {id} not found")
        else:
            return

    return hadith_info


def UpdateHadith(session: Session, id: int, info_update: CreateAndUpdateHadith, token_info):
    from cruds.hadith_assesment import UpdateHadithAssesmentInfo, CreateHadithAssesmentInfo

    hadith_info = GetHadithById(session, id)

    try:
        hadith_assesment_info = session.query(HadithAssesment).where(
            HadithAssesment.hadith_id == id, HadithAssesment.user_id == token_info.id).first()
        UpdateHadithAssesmentInfo(
            session, hadith_assesment_info.id,  # type: ignore
            UpdateHadithAssesment(evaluation_id=info_update.evaluation_id),
            token_info
        )
    except:
        CreateHadithAssesmentInfo(
            session,
            CreateHadithAssesment(
                hadith_id=id,
                evaluation_id=info_update.evaluation_id,
            ),
            token_info)

    hadith_info.updated_by = token_info.id  # type: ignore
    for attr, value in info_update.__dict__.items():
        setattr(hadith_info, attr, value)
    session.commit()
    session.refresh(hadith_info)
    return hadith_info.__dict__


def DeleteHadith(session: Session, id: int):
    hadith_info = GetHadithById(session, id)
    hadith_assesment = session.query(HadithAssesment).filter(
        HadithAssesment.hadith_id == id).all()
    for assesment in hadith_assesment:
        session.delete(assesment)
    session.delete(hadith_info)
    session.commit()
    return f'Hadith id "{id}" deleted success'
