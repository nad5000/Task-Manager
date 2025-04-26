from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.utils import get_curr_time, get_uuid
from utils.db_utils import DBManager
import uvicorn
import os
from fastapi import status


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_CONFIG = {DB_HOST}
SERVER_HOSTNAME = "0.0.0.0"
SERVER_PORT = 8001


class TaskID(BaseModel):
    task_id: str


class Task(BaseModel):
    title: str
    description: str
    assignee: str


manager = DBManager(DB_HOST)


app = FastAPI()


@app.get("/get_tasks")
async def get_tasks():
    """
    get list of tasks
    """
    await manager.connect()
    tasks = await manager.get_all_tasks()
    await manager.close()
    return JSONResponse(content=tasks, status_code=200)

@app.post("/add_task/",status_code=status.HTTP_201_CREATED)
async def add_task(task: Task):
    """
    insert a new task
    """
    await manager.connect()
    await manager.insert_task(**task.model_dump(), creation_time=get_curr_time(), task_id=get_uuid())
    await manager.close()

@app.delete("/remove_task/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_task(item_id: TaskID):
    """
    remove a task
    """
    await manager.connect()
    await manager.del_task(**item_id.model_dump())
    await manager.close()


if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_HOSTNAME, port=SERVER_PORT)