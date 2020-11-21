#!/bin/sh
echo "Creating schema..."
docker exec -it $(docker ps -q --filter="NAME=cassandra*") cqlsh -f scripts/cassandra/1-keyspace-tables.sql
echo "Executing inserts..."
docker exec -it $(docker ps -q --filter="NAME=cassandra*") cqlsh -f scripts/cassandra/2-copy.sql
echo "Done"