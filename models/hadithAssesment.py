from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class HadithAssesment(Base):
    __tablename__ = "hadith_assesment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserInfo", back_populates="evaluations")
    hadith_id = Column(Integer, ForeignKey("hadith.id"))
    hadith = relationship("Hadith", back_populates="evaluations")
    evaluation_id = Column(Integer, ForeignKey("type_hadith.id"))
    evaluation = relationship("TypeHadith", back_populates="evaluation")
