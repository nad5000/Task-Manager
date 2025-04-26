#!/bin/bash
echo "Waiting for db2 to be ready..."
until pg_isready -h db_2 -p 5432 -U postgres; do
  sleep 1
done

psql -U postgres -d postgres -c "
CREATE SUBSCRIPTION sub_from_db2
CONNECTION 'host=db_2 port=5432 user=replicator password=replicator dbname=postgres'
PUBLICATION pub_2
WITH (create_slot = false, slot_name = 'sub_from_db2', connect = false, origin = 'none');"
psql -U postgres -d postgres -c "
ALTER SUBSCRIPTION sub_from_db2 ENABLE;"
psql -U postgres -d postgres -c "
ALTER SUBSCRIPTION sub_from_db2 REFRESH PUBLICATION;"
