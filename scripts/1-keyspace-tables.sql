CREATE KEYSPACE mykeyspace
  WITH REPLICATION = { 
   'class' : 'NetworkTopologyStrategy', 
   'datacenter1' : 1 
  } ;

CREATE TABLE mykeyspace.person ( 
   id UUID PRIMARY KEY, 
   lastname text, 
   firstname text 
) ;