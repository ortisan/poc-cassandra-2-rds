DROP KEYSPACE IF EXISTS mykeyspace;


CREATE KEYSPACE IF NOT EXISTS mykeyspace
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'datacenter1' : 1 
  } ;

CREATE TYPE mykeyspace.phone (
  id UUID,
  phone_number int,
  description text,
  creation_date timestamp
);

CREATE TABLE IF NOT EXISTS mykeyspace.person ( 
   id UUID PRIMARY KEY, 
   lastname text, 
   firstname text,
   phones list<frozen<phone>>
) ;