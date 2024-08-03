from sqlalchemy.orm import Session
from models.model import Model
from fastapi import UploadFile, File
from utils import send_error_response, file_management
import os
import uuid
from typing import Optional
from sqlalchemy import or_


def CreateModel(session: Session, name: str, status: bool, file: UploadFile = File(...)):
    MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024  # 2mb
    # if file.content_type not in ['image/jpeg', 'image/png']:
    #     send_error_response(
    #         'Wrong file type, only accept jpeg or png',
    #         'Wrong file type, only accept jpeg or png'
    #     )
    if os.fstat(file.file.fileno()).st_size > MAX_FILE_SIZE_BYTES:
        send_error_response(
            'File too large, only accept file below 2mb',
            'File too large, only accept file below 2mb'
        )
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    upload_dir = os.path.join(base_dir, 'uploads/models')
    os.makedirs(upload_dir, exist_ok=True)
    file_extension = file.filename.split('.')[-1]  # type: ignore
    filename = f'{uuid.uuid4()}.{file_extension}'
    file_path = os.path.join(upload_dir, filename)
    try:
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
    except Exception as error:
        send_error_response(str(error), 'Failed to save file')
    if not os.path.exists(file_path):
        send_error_response(
            'File not found after saving',
            'File not found after saving'
        )
    if status:
        disabled_other_data = session.query(
            Model).filter(Model.status == True).all()
        for data in disabled_other_data:
            data.status = False  # type: ignore
        session.commit()
    add_new_data = Model(name=name, file=filename, status=status)
    session.add(add_new_data)
    session.commit()
    session.refresh(add_new_data)
    query_files = session.query(Model).all()
    file_management(query_files, upload_dir)
    return {
        "detail": "File uploaded successfully",
        "content_type": file.content_type,
        "file_name": filename,
        "data": add_new_data
    }


def GetAllModel(session: Session, limit: int, offset: int, search: Optional[str] = None):
    query = session.query(Model)
    if search:
        query = query.filter(or_(*[getattr(Model, column).ilike(
            f"%{search}%"
        ) for column in Model.__table__.columns.keys()]))
    return {
        "total_data": query.count(),
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": query.offset(offset).limit(limit).all()
    }


def GetModelById(session: Session, id: int):
    model_info = session.query(Model).get(id)
    if model_info is None:
        send_error_response(
            f"Model id {id} not found",
            f"Model id {id} not found"
        )
    return model_info


def UpdateModel(session: Session, id: int, name: str, status: bool, file: UploadFile = File(...)):
    model_info = GetModelById(session, id)
    MAX_FILE_SIZE_BYTES = 2 * 1024 * 1024  # 2mb
    # if file.content_type not in ['image/jpeg', 'image/png']:
    #     send_error_response(
    #         'Wrong file type, only accept jpeg or png',
    #         'Wrong file type, only accept jpeg or png'
    #     )
    if os.fstat(file.file.fileno()).st_size > MAX_FILE_SIZE_BYTES:
        send_error_response(
            'File too large, only accept file below 2mb',
            'File too large, only accept file below 2mb'
        )
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    upload_dir = os.path.join(base_dir, 'uploads/models')
    os.makedirs(upload_dir, exist_ok=True)
    file_extension = file.filename.split('.')[-1]  # type: ignore
    filename = f'{uuid.uuid4()}.{file_extension}'
    file_path = os.path.join(upload_dir, filename)
    try:
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
    except Exception as error:
        send_error_response(str(error), 'Failed to save file')
    if not os.path.exists(file_path):
        send_error_response(
            'File not found after saving',
            'File not found after saving'
        )
    if status:
        disabled_other_data = session.query(
            Model).filter(Model.status == True).all()
        for data in disabled_other_data:
            data.status = False  # type: ignore
        session.commit()
    model_info.file = filename  # type: ignore
    model_info.name = name  # type: ignore
    model_info.status = status  # type: ignore
    session.commit()
    session.refresh(model_info)
    query_files = session.query(Model).all()
    file_management(query_files, upload_dir)
    return {
        "detail": "File uploaded successfully",
        "content_type": file.content_type,
        "file_name": filename,
        "data": model_info.__dict__
    }


def DeleteModel(session: Session, id: int):
    model_info = GetModelById(session, id)
    session.delete(model_info)
    session.commit()
    return {"detail": "Model deleted successfully"}
