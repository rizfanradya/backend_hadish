from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Text
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
    hadith_arab = Column(Text)
    hadith_melayu = Column(Text)
    explanation = Column(Text)
    evaluations = relationship("HadithAssesment", back_populates="hadith")
