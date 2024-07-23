from datetime import datetime, timedelta
from typing import Union, Any
import jwt
import os
from dotenv import load_dotenv
import calendar

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 60 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = os.environ.get('JWT_REFRESH_SECRET_KEY')
IP_SERVER_HOSTNAME = os.environ.get('IP_SERVER_HOSTNAME')
SERVER_PORT = os.environ.get('SERVER_PORT')
DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')


# print('JWT_SECRET_KEY', JWT_SECRET_KEY)
# print('JWT_REFRESH_SECRET_KEY', JWT_REFRESH_SECRET_KEY)
# print('IP_SERVER_HOSTNAME', IP_SERVER_HOSTNAME)
# print('SERVER_PORT', SERVER_PORT)
# print('DB_HOSTNAME', DB_HOSTNAME)
# print('DB_PORT', DB_PORT)
# print('DB_USER', DB_USER)
# print('DB_PASSWORD', DB_PASSWORD)
# print('DB_NAME', DB_NAME)


def create_access_token(subject: Union[str, Any], expires_delta=None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    encoded_jwt = jwt.encode(payload={"exp": expires_delta, "id": str(subject)},
                             key=str(JWT_SECRET_KEY),
                             algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta=None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    encoded_jwt = jwt.encode(payload={"exp": expires_delta, "id": str(subject)},
                             key=str(JWT_REFRESH_SECRET_KEY),
                             algorithm=ALGORITHM)
    return encoded_jwt
