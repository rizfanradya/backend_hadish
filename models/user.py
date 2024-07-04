from sqlalchemy.schema import Column
from sqlalchemy.types import String, Boolean, Integer, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class UserInfo(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    username = Column(String(length=100), unique=True, nullable=False)
    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255))
    email = Column(String(length=255))
    password = Column(String(length=300), nullable=False)
    status = Column(Boolean)
    role = Column(Integer, nullable=False)
    evaluations = relationship("HadithAssesment", back_populates="user")
