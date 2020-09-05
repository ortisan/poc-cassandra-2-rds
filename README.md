# Cassandra 2 Rds

This is a POC for migrate data from cassandra to RDS.

Pre-reqs:

1. Cassandra environment (We provide with docker)
2. AWS cli. Data migration needs upload files to S3


Steps:

1. Generate data

```sh
python3 src/inserts-generator.py
```

2. Create a keyspace and inserts

```sh
./script-in.sh
```
3. Export data

```sh
./script-out.sh
```