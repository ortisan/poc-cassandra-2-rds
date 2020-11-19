# Cassandra 2 Rds

This is a POC for migrate data from cassandra to RDS.

Pre-reqs:

1. Cassandra environment (We provide with docker)
2. AWS cli. Data migration needs upload files to S3


## Steps:

### Environment
   1. Create and enable Python Virtual Environment:
      ```sh
      virtualenv env
      source env/bin/activate
      pip install -r requirements.txt
      ``` 

### Cassandra Environment

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

### AWS Environment:

   1. Package lambda
      ```sh
      cd aws/lambdas/create_tables
      virtualenv env
      source env/bin/activate
      pip install -r requirements.txt 
      cd env/lib/python3.8/site-packages
      zip -r lambda_create_table.zip .
      cd ../../../../
      zip -g lambda_create_table.zip lambda_function.py
      ``` 
   1. Create Buckets Stack
      ```sh
      python3 src/create_buckets.py
      ```
   1. Upload lambdas
      ```sh
      python3 src/upload_lambdas_bucket.py
      ```   
   1. Create RDS Stack
      ```sh
      python3 src/create_rds.py
      ```  
   1. Upload Cassandra Data to S3
      ```sh
      python3 src/upload2bucket.py
      ```
   1. Create an rds
      ```sh
      python3 src/create_rds.py
      ```
   1. Create a roles for Aws Lambdas with permitions of Secrets Manager, System Manager, RDS and S3.

   1. Upload the lambdas functions on S3
      ```sh
      python3 src/upload_lambdas_bucket.py
      ```
   1. Create the Lambdas
      ```sh
      python3 src/create_functions.py
      ```


### Usable commands and links:

1. Cassandra User Defined Type:
https://docs.datastax.com/en/dse/6.7/cql/cql/cql_using/useCreateUDT.html

1. Optimization of Cassandra COPY:
https://www.datastax.com/blog/six-parameters-tune-cqlsh-copy-performance

1. Deployable lambda: 
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

1. Glue sample: 
https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html


#### TODO:
1. Job Glue




aws secretsmanager get-secret-value --secret-id DatabaseRotationSecret
aws ssm get-parameter --name "DatabaseEndpointUrl"

admin

docker run -it mysql mysql -h rdstest.cn9vnkebenrp.us-east-1.rds.amazonaws.com -P 3306 -u admin -pX1xS45zZjrsl1Onx

X1xS45zZjrsl1Onx

rdstest.cn9vnkebenrp.us-east-1.rds.amazonaws.com

jdbc:mysql://rdstest.cn9vnkebenrp.us-east-1.rds.amazonaws.com:3306/persondb
Criar Crawler


rdstest.cn9vnkebenrp.us-east-1.rds.amazonaws.com:3306/persondb
rdstest.cn9vnkebenrp.us-east-1.rds.amazonaws.com