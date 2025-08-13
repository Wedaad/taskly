from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Defines a task object 
class Task(BaseModel):
    name: str
    description: Union[str, None] = None
    task_id: int
    progress: str = "Not Started"
    duedate: Union[str, None] = None

tasks = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return tasks

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task_with_id(task_id: int):
    return {"task_id": task_id, "name": "Sample Task", "description": "This is a sample task.", "progress": "In Progress", "duedate": "2023-12-31"}