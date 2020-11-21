# Cassandra 2 Rds

This is a POC for migrate data from cassandra to RDS.

Pre-reqs:

1. Cassandra and BigData environment - docker-compose
2. AWS cli. Data migration needs upload files to S3

## Steps:

### Environment
   1. Create and enable Python Virtual Environment:
      ```sh
      virtualenv env
      source env/bin/activate
      pip install -r requirements.txt
      ``` 

### Preparing BigData Environment

1. Starting environment:
   ```sh
   docker-compose up -d
   ```
1. Generate Cassandra data
   ```sh
   python3 src/inserts-generator.py
   ```
1. Create a Cassandra keyspace and inserts
   ```sh
   ./scripts/cassandra/script-input-data-cassandra.sh
   ```
1. Export Cassandra data
   ```sh
   ./scripts/cassandra/script-ouput-data-cassandra.sh
   ```

### Jobs

https://github.com/tentativafc/cassandra-2-rds/blob/master/data/jupyter/work/PersonETLJob.ipynb

Edit into jupyter notebook - http://localhost:8888


Show token:

```sh
docker logs jupyter 
```

### Results

Use adminer to view results:

http://localhost:8080/?server=mysql&username=mama&db=mydatabase&sql=select%20*%20from%20person%0A%0A


http://localhost:8080/?server=mysql&username=mama&db=mydatabase&sql=select%20*%20from%20phone%3B


### Usable commands and links:

1. Cassandra User Defined Type:
https://docs.datastax.com/en/dse/6.7/cql/cql/cql_using/useCreateUDT.html

1. Optimization of Cassandra COPY:
https://www.datastax.com/blog/six-parameters-tune-cqlsh-copy-performance

1. Deployable lambda: 
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

1. Glue sample: 
https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html



















