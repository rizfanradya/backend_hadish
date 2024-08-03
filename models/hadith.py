from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Text
from database import Base
from sqlalchemy.orm import relationship


class Hadith(Base):
    __tablename__ = "hadith"

    id = Column(Integer, primary_key=True, index=True)
    hadith_arab = Column(Text)
    hadith_melayu = Column(Text)
    explanation = Column(Text)
    evaluations = relationship("HadithAssesment", back_populates="hadith")
