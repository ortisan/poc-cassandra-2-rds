#!/bin/sh
echo "Creating schema..."
#docker exec -it $(docker ps -q --filter="NAME=cassandra*") cqlsh -f scripts/1-keyspace-tables.sql
echo "Executing inserts..."
docker exec -it $(docker ps -q --filter="NAME=cassandra*") cqlsh -f scripts/2-copy.sql
echo "Done"