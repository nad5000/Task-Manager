#!/bin/bash
echo "Waiting for db1 to be ready..."
until pg_isready -h db_1 -p 5432 -U postgres; do
  sleep 1
done

psql -U postgres -d postgres -c "
CREATE SUBSCRIPTION sub_from_db1
CONNECTION 'host=db_1 port=5432 user=replicator password=replicator dbname=postgres'
PUBLICATION pub_1
WITH (create_slot = false, slot_name = 'sub_from_db1', connect = false, origin = 'none');"
psql -U postgres -d postgres -c "
ALTER SUBSCRIPTION sub_from_db1 ENABLE;"
psql -U postgres -d postgres -c "
ALTER SUBSCRIPTION sub_from_db1 REFRESH PUBLICATION;"