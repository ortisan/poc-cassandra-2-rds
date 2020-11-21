-- Absolute path based on Cassandra docker volume
COPY mykeyspace.person FROM '/data/person-in.csv' WITH DELIMITER=',';
