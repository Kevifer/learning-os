from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_

from database import Base, engine, SessionLocal
from models import Goal, Task
from schemas import GoalCreate, TaskCreate


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


@app.get("/goals")
def get_goals(search: str | None = None, db: Session = Depends(get_db)):
    if search:
        return db.query(Goal).filter(
	or_(	
		Goal.name.like(f"%{search}%"),
		Goal.description.like(f"%{search}%")
	)
	).all()
    else:
        return db.query(Goal).all()

@app.get("/goals/{goal_id}")
def get_goal_by_id(goal_id: int, db: Session = Depends(get_db)):
    return db.query(Goal).filter(Goal.id == goal_id).first()


@app.post("/goals/{goal_id}/tasks")
def create_task(goal_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description,
        goal_id=goal_id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task
