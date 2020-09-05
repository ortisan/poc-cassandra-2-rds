#!/bin/sh
echo "Creating schema..."
cqlsh -f scripts/1-keyspace-tables.sql
echo "Executing inserts..."
cqlsh -f scripts/2-copy.sql
echo "Done"