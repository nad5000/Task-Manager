CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'replicator';

CREATE TABLE IF NOT EXISTS tasks (
    task_id TEXT,
    assignee TEXT,
    title TEXT,
    description TEXT,
    creation_time TEXT
);
GRANT SELECT ON tasks TO postgres;
GRANT SELECT ON tasks TO replicator;

ALTER TABLE tasks REPLICA IDENTITY FULL;

CREATE PUBLICATION pub_1 FOR TABLE tasks;
SELECT * FROM pg_create_logical_replication_slot('sub_from_db1', 'pgoutput');
