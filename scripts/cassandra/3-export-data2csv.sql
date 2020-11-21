-- Absolute path based on Cassandra docker volume
COPY mykeyspace.person (id, lastname, firstname, phones) TO '/data/person-out.csv' WITH HEADER = TRUE;