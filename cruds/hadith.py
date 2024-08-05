from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from schemas.hadith_assesment import UpdateHadithAssesment, CreateHadithAssesment
from models.hadith import Hadith
from models.hadithAssesment import HadithAssesment
from models.typehadith import TypeHadith
from typing import Optional
from sqlalchemy import or_, func, and_
from fastapi import File, UploadFile, HTTPException
import pandas as pd
from io import StringIO
from starlette.responses import StreamingResponse
import csv
from utils import send_error_response


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
    if not file.filename.endswith('.csv'):  # type: ignore
        send_error_response(
            "Invalid file format",
            "File must be in CSV format"
        )

    try:
        df = pd.read_csv(file.file)
    except Exception:
        try:
            file.file.seek(0)
            csv_data = file.file.read().decode('utf-8')
            file_string = StringIO(csv_data)
            df = pd.read_csv(file_string)
        except Exception as error:
            send_error_response(str(error), "Could not read the CSV file.")

    valid_evaluation_ids = {
        type.id for type in session.query(TypeHadith).all()}
    invalid_ids = df[~df['evaluation_id'].isin(
        valid_evaluation_ids)]['evaluation_id'].unique()
    if invalid_ids.size > 0:
        send_error_response(
            f"Invalid evaluation id(s): {', '.join(map(str, invalid_ids))}",
            f"Invalid evaluation id(s): {', '.join(map(str, invalid_ids))}"
        )

    try:
        df = df.fillna('')
        hadith_entries = []
        hadith_assessment_entries = []

        for _, row in df.iterrows():
            hadith_entry = Hadith(
                hadith_arab=row['hadish_arab'],
                hadith_melayu=row['hadish_melayu'],
                explanation=row['keterangan'],
            )
            hadith_entries.append(hadith_entry)

        session.add_all(hadith_entries)
        session.commit()
        for hadith_entry in hadith_entries:
            session.refresh(hadith_entry)

        for _, row in df.iterrows():
            hadith = next(
                (
                    entry for entry in hadith_entries
                    if entry.hadith_arab == row['hadish_arab']
                    and entry.hadith_melayu == row['hadish_melayu']
                    and entry.explanation == row['keterangan']
                ), None
            )
            if hadith:
                hadith_assessment = HadithAssesment(
                    hadith_id=hadith.id,
                    evaluation_id=row['evaluation_id'],
                    user_id=token_info.id
                )
                hadith_assessment_entries.append(hadith_assessment)

        session.add_all(hadith_assessment_entries)
        session.commit()
        for hadith_assessment_entry in hadith_assessment_entries:
            session.refresh(hadith_assessment_entry)

    except Exception as error:
        send_error_response(str(error), "Invalid CSV format")
    return hadith_entries


def DownloadTemplate(session: Session):
    type_hadith = session.query(TypeHadith).all()
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "no",
        "hadish_arab",
        "hadish_melayu",
        "keterangan",
        "evaluation_id",
    ])
    writer.writerow(["", "", "", "", "", "", "", "id", "evaluation"])
    for type in type_hadith:
        writer.writerow(["", "", "", "", "", "", "",
                        f"{type.id}", f"{type.type}"])
    buffer.seek(0)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=format_hadith.csv"}
    )


def DownloadHadith(session: Session):
    # Compute the count of each evaluation for every Hadith
    # Hitung jumlah setiap evaluasi untuk setiap Hadis
    hadith_evaluation_counts = session.query(
        Hadith.id.label('hadith_id'),
        HadithAssesment.evaluation_id,
        func.count(HadithAssesment.evaluation_id).label('count')
    ).join(HadithAssesment, Hadith.id == HadithAssesment.hadith_id).group_by(
        Hadith.id, HadithAssesment.evaluation_id
    ).cte('hadith_evaluation_counts')

    # Determine the maximum count for each Hadith
    # Tentukan jumlah maksimal setiap hadis
    max_counts = session.query(
        hadith_evaluation_counts.c.hadith_id,
        func.max(hadith_evaluation_counts.c.count).label('max_count')
    ).group_by(hadith_evaluation_counts.c.hadith_id).cte('max_counts')

    # Find the evaluations that have the maximum count for each Hadith
    # Temukan evaluasi yang memiliki jumlah maksimum untuk setiap Hadis
    most_frequent_evaluation = session.query(
        hadith_evaluation_counts.c.hadith_id,
        hadith_evaluation_counts.c.evaluation_id,
        hadith_evaluation_counts.c.count
    ).join(
        max_counts, and_(
            hadith_evaluation_counts.c.hadith_id == max_counts.c.hadith_id,
            hadith_evaluation_counts.c.count == max_counts.c.max_count
        )
    ).cte('most_frequent_evaluation')

    # Filter out Hadith with unique most frequent evaluation
    # Saring Hadits dengan evaluasi unik yang paling sering
    unique_evaluations = session.query(
        most_frequent_evaluation.c.hadith_id
    ).group_by(
        most_frequent_evaluation.c.hadith_id
    ).having(
        func.count(most_frequent_evaluation.c.evaluation_id) == 1
    ).subquery()

    # Fetch the filtered Hadith and their evaluations
    # Ambil Hadits yang disaring dan evaluasinya
    filtered_hadith = session.query(Hadith, TypeHadith).select_from(Hadith).join(
        unique_evaluations, Hadith.id == unique_evaluations.c.hadith_id
    ).join(
        most_frequent_evaluation, Hadith.id == most_frequent_evaluation.c.hadith_id
    ).join(
        TypeHadith, most_frequent_evaluation.c.evaluation_id == TypeHadith.id
    ).all()

    # Create a DataFrame from the results
    # Buat DataFrame dari hasilnya
    df = pd.DataFrame([{
        "id": hadith.id,
        "Hadith Arab": hadith.hadith_arab,
        "Hadith Melayu": hadith.hadith_melayu,
        "Explanation": hadith.explanation,
        "Evaluation": type_hadith.type
    } for hadith, type_hadith in filtered_hadith])

    df = df.sort_values(by="id")
    output = StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=hadith_data.csv"}
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
