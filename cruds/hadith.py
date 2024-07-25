from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from schemas.hadith_assesment import UpdateHadithAssesment, CreateHadithAssesment
from models.hadith import Hadith
from models.hadithAssesment import HadithAssesment
from models.typehadith import TypeHadith
from typing import Optional
from sqlalchemy import or_, func, and_, not_, select
from fastapi import File, UploadFile, HTTPException
import pandas as pd
from io import BytesIO
from starlette.responses import FileResponse, StreamingResponse
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
    keywords = 'maud'
    search_terms = keywords.split()
    query = session.query(TypeHadith)
    conditions = [TypeHadith.type.ilike(f'%{term}%') for term in search_terms]
    hadith_maudhuk_info = query.filter(or_(*conditions)).first()

    if hadith_maudhuk_info is None:
        raise HTTPException(
            status_code=404, detail=f"Hadith 'Maudhuk' not found")

    subquery = select(HadithAssesment.hadith_id).filter(
        HadithAssesment.evaluation_id == hadith_maudhuk_info.id
    ).subquery()

    hadith_evaluation_counts = session.query(
        Hadith.id.label('hadith_id'),
        HadithAssesment.evaluation_id,
        func.count(HadithAssesment.evaluation_id).label('count')
    ).join(HadithAssesment, Hadith.id == HadithAssesment.hadith_id).filter(
        not_(Hadith.id.in_(select(subquery)))
    ).group_by(
        Hadith.id, HadithAssesment.evaluation_id
    ).cte('hadith_evaluation_counts')

    max_counts = session.query(
        hadith_evaluation_counts.c.hadith_id,
        func.max(hadith_evaluation_counts.c.count).label('max_count')
    ).group_by(hadith_evaluation_counts.c.hadith_id).cte('max_counts')

    most_frequent_evaluation = session.query(
        hadith_evaluation_counts.c.hadith_id, hadith_evaluation_counts.c.evaluation_id
    ).join(
        max_counts, and_(
            hadith_evaluation_counts.c.hadith_id == max_counts.c.hadith_id,
            hadith_evaluation_counts.c.count == max_counts.c.max_count
        )
    ).distinct(hadith_evaluation_counts.c.hadith_id).subquery()

    all_hadith = session.query(Hadith, TypeHadith).select_from(Hadith).join(
        most_frequent_evaluation, Hadith.id == most_frequent_evaluation.c.hadith_id
    ).join(TypeHadith, most_frequent_evaluation.c.evaluation_id == TypeHadith.id).all()

    df = pd.DataFrame([{
        "Hadith Arab": hadith.hadith_arab,
        "Hadith Melayu": hadith.hadith_melayu,
        "Explanation": hadith.explanation,
        "Type": type_hadith.type
    } for hadith, type_hadith in all_hadith])

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Hadith Data')
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=hadith_data.xlsx"}
    )


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
