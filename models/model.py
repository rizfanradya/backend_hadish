from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Boolean
from database import Base


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), nullable=False)
    file = Column(String(length=255), nullable=False)
    status = Column(Boolean, nullable=False, default=False)
