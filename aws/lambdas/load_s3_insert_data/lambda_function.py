import boto3
import os
import sys
import uuid
import glob
from urllib.parse import unquote_plus
import config
import pymysql
import logging

#rds settings
rds_host  = config.rds_endpoint
name = config.db_username
password = config.db_password
db_name = config.db_name
s3_bucket = config.bucket_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

s3_client = boto3.client('s3')

response = s3_client.list_objects(Bucket=s3_bucket)
contents = response['Contents']
files = [f['Key'] for f in contents]    
# for file in files[1:2]:
#     download_path = '/tmp/{}'.format(file)
#     s3_client.download_file(s3_bucket, file, download_path)
files = glob.glob("/tmp/split_person*")
for file in files:
    filename = os.path.basename(file)    
    #script = "select * from person"
    script = "LOAD DATA INFILE '/tmp/{}' INTO TABLE person FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n';".format(file)
    with conn.cursor() as cur:
        response = cur.execute(script)
        print(response)
        conn.commit()
    

def lambda_handler(event, context):
    pass
   


