from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Goal
from schemas import GoalCreate

app = FastAPI(title="Learning OS")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {
        "message": "Learning OS is alive!"
    }


@app.post("/goals")
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    new_goal = Goal(
        name=goal.name,
        description=goal.description
    )

    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)

    return new_goal
