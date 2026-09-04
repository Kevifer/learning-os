from pydantic import BaseModel


class GoalCreate(BaseModel):
    name: str
    description: str | None = None

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
