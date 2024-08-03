from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base
from sqlalchemy.orm import relationship


class TypeHadith(Base):
    __tablename__ = "type_hadith"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(length=255), unique=True, nullable=False)
    evaluation = relationship("HadithAssesment", back_populates="evaluation")
