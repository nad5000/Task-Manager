import psycopg2


class DBManager:
    def __init__(self):
        pass


    def _connect(self):
        self.conn = psycopg2.connect(
            host="0.0.0.0",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        self.cur = self.conn.cursor()

    def _disconnect(self):
        self.cur.close()
        self.conn.close()

    def insert_task(self, task_id, assignee, title, description, creation_time):
        self._connect()
        insert_query = """
                       INSERT INTO tasks (task_id, assignee, title, description, creation_time)
                       VALUES (%s, %s, %s, %s, %s); \
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
        self.cur.execute(create_table_query)
        self.conn.commit()
        self.cur.execute(insert_query, (task_id, assignee, title, description, creation_time))
        self.conn.commit()
        self._disconnect()

    def get_all_tasks(self):
        self._connect()
        self.cur.execute("SELECT * FROM tasks;")
        tasks = self.cur.fetchall()
        self._disconnect()
        return tasks

    def del_task(self, task_id):
        self._connect()
        delete_query = """
                       DELETE FROM tasks WHERE task_id = %s;
                       """
        self.cur.execute(delete_query, (task_id,))
        self.conn.commit()
        self._disconnect()


