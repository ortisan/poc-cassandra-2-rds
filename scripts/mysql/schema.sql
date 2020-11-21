DROP TABLE IF EXISTS phone, mydatabase.person;
CREATE TABLE person (id VARCHAR(36), first_name VARCHAR(100), last_name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE phone (id VARCHAR(36), person_id VARCHAR(36), phone_number int, PRIMARY KEY (id), FOREIGN KEY (person_id) REFERENCES person(id));
