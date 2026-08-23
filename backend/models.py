from sqlalchemy import Column, Integer, String

from database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
