from sqlalchemy.schema import Column
from sqlalchemy.types import String, Boolean, Integer, DateTime
from database import Base


class UserInfo(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    username = Column(String(length=100), unique=True, nullable=False)
    email = Column(String(length=255))
    password = Column(String(length=300), nullable=False)
    status = Column(Boolean)
    role = Column(Integer, nullable=False)
