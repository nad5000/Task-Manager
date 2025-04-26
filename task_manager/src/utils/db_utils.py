import asyncpg
from typing import Dict, List


class DBManager:
    def __init__(self, db_host: str, port: int = 5432):
        self.db_host = db_host
        self.port = port


    async def connect(self) -> None:
        self.conns = await asyncpg.create_pool(host=self.db_host,
            port=self.port,
            database="postgres",
            user="postgres",
            password="postgres")

    async def close(self) -> None:
        self.conns.close()

    async def create_tasks_table(self) -> None:
        """
        create tasks table if it doesn't exist
        """
        create_table_query = """
                             CREATE TABLE IF NOT EXISTS tasks \
                             ( \
                                 task_id TEXT,
                                 assignee TEXT,
                                 title TEXT,
                                 description TEXT,
                                 creation_time TEXT
                                 ); \
                             """
        async with self.conns.acquire() as conn:
            await conn.execute(create_table_query)

    async def insert_task(self, task_id: str, assignee: str, title: str, description: str, creation_time: str) -> None:
        """
        insert a new task
        :param task_id: the task id of the new task
        :param assignee: assignee username
        :param title: the title of the task
        :param description: the description of the task
        :param creation_time: creation time
        """
        insert_query = """
                       INSERT INTO tasks (task_id, assignee, title, description, creation_time)
                       VALUES ($1, $2, $3, $4, $5); \
                       """
        async with self.conns.acquire() as conn:
            await conn.execute(insert_query, task_id, assignee, title, description, creation_time)

    async def get_all_tasks(self) -> List[Dict[str, str]]:
        """
        get all tasks from db
        :return: list of tasks
        """
        async with self.conns.acquire() as conn:
            tasks = await conn.fetch("SELECT * FROM tasks;")
            return [dict(task) for task in tasks]

    async def del_task(self, task_id: str) -> None:
        """
        delete a task from db
        :param task_id: the task id of the task
        """
        delete_query = """
                       DELETE FROM tasks WHERE task_id = $1;
                       """
        async with self.conns.acquire() as conn:
            await conn.execute(delete_query, task_id,)
