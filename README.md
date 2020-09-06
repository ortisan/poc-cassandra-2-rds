# Cassandra 2 Rds

This is a POC for migrate data from cassandra to RDS.

Pre-reqs:

1. Cassandra environment (We provide with docker)
2. AWS cli. Data migration needs upload files to S3


Steps:

1. Create and enable Python Virtual Environment:
   ```sh
   virtualenv env
   source env/bin/activate
   pip install -r requirements.txt
   ``` 
1. Starting Cassandra environment:
   ```sh
   docker-compose up -d
   ```
1. Generate data
   ```sh
   python3 src/inserts-generator.py
   ```
1. Create a keyspace and inserts
   ```sh
   ./script-in.sh
   ```
1. Export data
   ```sh
   ./script-out.sh
   ```
1. Upload backup file
   ```sh
   python3 src/upload2bucket.py
   ```
1. Create an rds
   ```sh
   python3 src/create-rds.py
   ```
1. Execute Aws Datapipeline or Aws lambda? 
   TODO