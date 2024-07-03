from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class TypeHadith(Base):
    __tablename__ = "type_hadith"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    type = Column(String(length=255), unique=True, nullable=False)
    evaluation = relationship(
        "HadithAssesment", back_populates="evaluation_id")
