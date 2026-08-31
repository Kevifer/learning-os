from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    goal_id = Column(Integer, ForeignKey("goals.id"))
