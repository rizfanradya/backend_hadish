from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Hadith(Base):
    __tablename__ = "hadith"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    hadith = Column(String(length=255))
    explanation = Column(String(length=255))
    evaluations = relationship("HadithAssesment", back_populates="hadith")
