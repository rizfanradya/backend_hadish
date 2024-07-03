from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class HadithAssesment(Base):
    __tablename__ = "hadith_assesment"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)
    updated_by = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserInfo", back_populates="evaluations")
    hadith_id = Column(Integer, ForeignKey("hadith.id"))
    hadith = relationship("hadith", back_populates="evaluations")
    evaluation_id = Column(Integer, ForeignKey("type_hadith.id"))
    evaluation = relationship("type_hadith", back_populates="evaluation")
