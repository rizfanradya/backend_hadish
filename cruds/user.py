from sqlalchemy.orm import Session
from schemas.user import CreateUser, UpdateUser
from fastapi import HTTPException
from password_validator import PasswordValidator
import hashlib
from models.user import UserInfo
from email_validator import validate_email, EmailNotValidError
from utils import format_datetime, create_access_token, create_refresh_token, ALGORITHM, JWT_SECRET_KEY, JWT_REFRESH_SECRET_KEY
from typing import Optional
from sqlalchemy import or_
import jwt

schema_password_validator = PasswordValidator()
schema_password_validator.min(8).has().uppercase(
).has().lowercase().has().digits().has().symbols()


def create_user(session: Session, user_info: CreateUser):
    from cruds.role import GetRoleByRole

    role_info = GetRoleByRole(session, 'USER', False)

    if user_info.password != user_info.confirm_password:
        raise HTTPException(
            status_code=404, detail="Password are not the same")

    password_validation = schema_password_validator.validate(
        user_info.password)

    if password_validation:
        try:
            validate_email(
                user_info.email, check_deliverability=False).normalized

            try:
                encode_password = user_info.password.encode()
                hash_password = hashlib.md5(encode_password).hexdigest()
                user_data = user_info.dict(exclude={'confirm_password'})

                new_user_info = UserInfo(**user_data)
                new_user_info.password = hash_password  # type: ignore
                new_user_info.role = new_user_info.role if new_user_info.role else role_info.id  # type: ignore
                new_user_info.status = True  # type: ignore

                session.add(new_user_info)
                session.commit()
                session.refresh(new_user_info)

                new_user_info.id
                return new_user_info

            except Exception as error:
                raise HTTPException(
                    status_code=404, detail=f'User "{user_info.username}" is already exist')

        except EmailNotValidError as error:
            raise HTTPException(status_code=404, detail="Email not valid")

    else:
        raise HTTPException(
            status_code=404,
            detail="Password must consist of at least 8 characters, contain at least one uppercase letter, one lowercase letter, one digit, one special character or symbol, and cannot contain spaces"
        )


def get_all_user(session: Session, limit: int, offset: int, search: Optional[str] = None):
    from models.role import Role

    all_user = session.query(UserInfo)
    role_info = session.query(Role).all()
    role_mapping = {role.id: role for role in role_info}

    if search:
        all_user = all_user.filter(or_(*[getattr(UserInfo, column).ilike(
            f"%{search}%"
        ) for column in UserInfo.__table__.columns.keys()]))  # type: ignore

    total_data = all_user.count()
    all_user = all_user.offset(offset).limit(limit).all()  # type: ignore

    for user in all_user:
        user.password = ''  # type: ignore
        user.created_by_name = session.query(UserInfo).get(
            user.created_by).username if session.query(UserInfo).get(user.created_by) else None  # type: ignore
        user.updated_by_name = session.query(UserInfo).get(
            user.updated_by).username if session.query(UserInfo).get(user.updated_by) else None  # type: ignore
        user.status_name = "ACTIVE" if user.status else "INACTIVE"  # type: ignore
        user.role_name = role_mapping.get(user.role).role if role_mapping.get(  # type: ignore
            user.role) else None
        user.created_at = format_datetime(user.created_at)  # type: ignore
        user.updated_at = format_datetime(user.updated_at)  # type: ignore

    return {
        "total_data": total_data,
        "limit": limit,
        "offset": offset,
        "search": search,
        "data": all_user
    }


def get_login(session: Session, user_login):
    user_info = session.query(UserInfo).where(
        UserInfo.username == user_login.username).first()
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")

    hash_password = hashlib.md5(user_login.password.encode()).hexdigest()
    if user_info.password == hash_password:  # type: ignore
        return {
            "id": user_info.id,
            "access_token": create_access_token(user_info.id),
            "refresh_token": create_refresh_token(user_info.id),
            "status": user_info.status,
            "detail": "ok"
        }
    else:
        return {
            "id": user_info.id,
            "access_token": "",
            "refresh_token": "",
            "status": False,
            "detail": "Username or Password incorrect"
        }


def get_user_by_id(session: Session, id: int, format: bool = True, error_handling: bool = True):
    from models.role import Role

    user_info = session.query(UserInfo).get(id)

    if user_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"User id {id} not found")
        else:
            return

    if format:
        user_info.password = ''
        user_info.created_by_name = session.query(UserInfo).get(
            user_info.created_by).username if session.query(UserInfo).get(user_info.created_by) else None  # type: ignore
        user_info.updated_by_name = session.query(UserInfo).get(
            user_info.updated_by).username if session.query(UserInfo).get(user_info.updated_by) else None  # type: ignore
        user_info.role_name = session.query(Role).get(
            user_info.role).role if session.query(Role).get(user_info.role) else None  # type: ignore
        user_info.status_name = "ACTIVE" if user_info.status else "INACTIVE"
        user_info.created_at = format_datetime(user_info.created_at)
        user_info.updated_at = format_datetime(user_info.updated_at)

    return user_info


def GetUserByUsername(session: Session, username: str, format: bool = True, error_handling: bool = True):
    from models.role import Role

    user_info = session.query(UserInfo).where(
        UserInfo.username == username).first()

    if user_info is None:
        if error_handling:
            raise HTTPException(
                status_code=404, detail=f"User {username} not found")
        else:
            return

    if format:
        user_info.password = ''  # type: ignore
        user_info.role_id = user_info.role
        user_info.created_by_name = session.query(UserInfo).get(
            user_info.created_by).username if session.query(UserInfo).get(user_info.created_by) else None  # type: ignore
        user_info.updated_by_name = session.query(UserInfo).get(
            user_info.updated_by).username if session.query(UserInfo).get(user_info.updated_by) else None  # type: ignore
        user_info.role_name = session.query(Role).get(
            user_info.role).role if session.query(Role).get(user_info.role) else None  # type: ignore
        user_info.status_name = "ACTIVE" if user_info.status else "INACTIVE"  # type: ignore
        user_info.created_at = format_datetime(  # type: ignore
            user_info.created_at)
        user_info.updated_at = format_datetime(  # type: ignore
            user_info.updated_at)

    return user_info


def update_user(session: Session, id: int, info_update: UpdateUser, token_info):
    from cruds.role import GetRoleById

    GetRoleById(session, info_update.role, False)
    user_info = get_user_by_id(session, id, False)

    if info_update.password != info_update.confirm_password:
        raise HTTPException(
            status_code=404, detail="Password are not the same")

    password_validation = schema_password_validator.validate(
        info_update.password)

    if password_validation:
        try:
            validate_email(
                user_info.email, check_deliverability=False).normalized  # type: ignore

            try:
                info_update.password = hashlib.md5(
                    info_update.password.encode()).hexdigest()
                user_info.updated_by = token_info.id  # type: ignore
                for attr, value in info_update.__dict__.items():
                    setattr(user_info, attr, value)

                session.commit()
                session.refresh(user_info)
                return user_info.__dict__

            except Exception as error:
                raise HTTPException(status_code=404, detail=f'{error}')

        except EmailNotValidError as error:
            raise HTTPException(status_code=404, detail="Email not valid")

    else:
        raise HTTPException(
            status_code=404,
            detail="Password must consist of at least 8 characters, contain at least one uppercase letter, one lowercase letter, one digit, one special character or symbol, and cannot contain spaces"
        )


def delete_user(session: Session, id: int):
    user_info = get_user_by_id(session, id, False)
    session.delete(user_info)
    session.commit()
    return f"User id {id} deleted success"


def TokenAuthorization(session: Session, token: str):
    if JWT_SECRET_KEY is None:
        raise EnvironmentError(f"Environment variable JWT_SECRET_KEY not set")

    try:
        decode_token = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM])

        user_info = session.query(UserInfo).get(decode_token.get('id'))
        if user_info is None:
            raise HTTPException(status_code=401, detail='User Not Found')
        return user_info

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Token is Invalid')


def RefreshToken(session: Session, refresh_token: str):
    if JWT_REFRESH_SECRET_KEY is None:
        raise EnvironmentError(f"Environment variable JWT_SECRET_KEY not set")

    try:
        decode_token = jwt.decode(
            refresh_token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM])

        user_info = session.query(UserInfo).get(decode_token.get('id'))
        if user_info is None:
            raise HTTPException(status_code=401, detail='User Not Found')

        return {
            "access_token": create_access_token(user_info.id),
            "refresh_token": create_refresh_token(user_info.id)
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Token is Invalid')
