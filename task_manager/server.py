from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from task_manager.utils.utils import get_curr_time, get_uuid
from task_manager.utils.db_utils import DBManager
import uvicorn


class TaskID(BaseModel):
    task_id: str


class Task(BaseModel):
    title: str
    description: str
    assignee: str


app = FastAPI()

@app.get("/get_tasks")
def get_tasks():
    manager = DBManager()
    return JSONResponse(content=manager.get_all_tasks(), status_code=200)

@app.post("/add_task/")
def add_task(task: Task):
    manager = DBManager()
    manager.insert_task(**task.model_dump(), creation_time=get_curr_time(), task_id=get_uuid())

@app.delete("/remove_task/")
def remove_task(item_id: TaskID):
    manager = DBManager()
    manager.del_task(**item_id.model_dump())

if __name__ == "__main__":
    uvicorn.run(app, host="10.100.102.23", port=8001)