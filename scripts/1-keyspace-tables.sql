CREATE KEYSPACE IF NOT EXISTS mykeyspace
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'datacenter1' : 1 
  } ;

CREATE TYPE mykeyspace.phone (
  id UUID,
  phone_number int
);

CREATE TABLE IF NOT EXISTS mykeyspace.person ( 
   id UUID PRIMARY KEY, 
   lastname text, 
   firstname text,
   phones list<frozen<phone>>
) ;