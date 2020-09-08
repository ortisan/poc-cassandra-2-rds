CREATE KEYSPACE IF NOT EXISTS mykeyspace
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'datacenter1' : 1 
  } ;

CREATE TABLE IF NOT EXISTS mykeyspace.person ( 
   id UUID PRIMARY KEY, 
   lastname text, 
   firstname text 
) ;