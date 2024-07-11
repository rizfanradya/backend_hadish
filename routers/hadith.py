from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.hadith import CreateAndUpdateHadith
from database import get_db
from typing import Optional
from cruds.hadith import CreateHadith, GetAllHadith, GetHadithById, UpdateHadith, DeleteHadith, UploadFileHadith, DownloadExcel, GetAllHadithEvaluate
from cruds.user import TokenAuthorization
from fastapi import File, UploadFile

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
router = APIRouter()


@router.post('/hadith')
def create_new_hadith(hadith_info: CreateAndUpdateHadith, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return CreateHadith(session, hadith_info, token_info)


@router.post('/hadith/upload')
async def upload_data_hadith(file: UploadFile = File(...), session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return await UploadFileHadith(session, token_info, file)


@router.get('/hadith/download')
def download_hadith_template(session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return DownloadExcel()


@router.get('/hadith')
def get_hadith(limit: int = 10, offset: int = 0, search: Optional[str] = None, filter_by: Optional[str] = 'all', number_of_appraisers: Optional[int] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetAllHadith(session, limit, offset,  filter_by, number_of_appraisers, search)


@router.get('/hadith/evaluate')
def get_hadith_evaluate(limit: int = 10, offset: int = 0, search: Optional[str] = None, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return GetAllHadithEvaluate(session, limit, offset, token_info, search)


@router.get("/hadith/{id}")
def get_hadith_by_id(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return GetHadithById(session, id)


@router.put("/hadith/{id}", response_model=CreateAndUpdateHadith)
def update_hadith(id: int, info_update: CreateAndUpdateHadith, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_info = TokenAuthorization(session, token)
    return UpdateHadith(session, id, info_update, token_info)


@router.delete("/hadith/{id}")
def delete_hadith(id: int, session: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    TokenAuthorization(session, token)
    return DeleteHadith(session, id)
