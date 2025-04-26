from task_manager.src.utils.db_utils import DBManager
from task_manager.src.utils.utils import get_curr_time, get_uuid
import pytest
import time


DBS_HOST = "localhost"
DB_2_PORT = 5433

@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_create_db():
    manager = DBManager(DBS_HOST)
    await manager.connect()
    await manager.close()

@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_create_task():
    manager = DBManager(DBS_HOST)
    await manager.connect()
    uuid = get_uuid()
    await manager.insert_task(title="title", description="description", assignee="assignee", creation_time=get_curr_time(), task_id=uuid)
    tasks = await manager.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "title"
    assert tasks[0]["description"] == "description"
    assert tasks[0]["assignee"] == "assignee"
    assert tasks[0]["task_id"] == uuid
    await manager.del_task(uuid)
    await manager.close()

@pytest.mark.order(3)
@pytest.mark.asyncio
async def test_del_task():
    manager = DBManager(DBS_HOST)
    await manager.connect()
    uuid = get_uuid()
    await manager.insert_task(title="title", description="description", assignee="assignee", creation_time=get_curr_time(), task_id=uuid)
    tasks = await manager.get_all_tasks()
    assert len(tasks) == 1
    await manager.del_task(uuid)
    tasks = await manager.get_all_tasks()
    assert len(tasks) == 0
    await manager.close()

@pytest.mark.order(4)
@pytest.mark.asyncio
async def test_sync_db():
    manager = DBManager(DBS_HOST)
    await manager.connect()
    uuid = get_uuid()
    await manager.insert_task(title="title", description="description", assignee="assignee", creation_time=get_curr_time(), task_id=uuid)
    await manager.close()
    time.sleep(5)
    manager_2 = DBManager(DBS_HOST, DB_2_PORT)
    await manager_2.connect()
    tasks = await manager_2.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "title"
    assert tasks[0]["description"] == "description"
    assert tasks[0]["assignee"] == "assignee"
    assert tasks[0]["task_id"] == uuid
    await manager_2.del_task(uuid)
    await manager_2.close()


