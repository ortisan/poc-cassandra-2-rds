import sys
import logging
import boto3
import json
import pymysql

db_endpoint_parameter_name = 'DatabaseEndpointUrl'
db_secret_name = 'DatabaseRotationSecret'
region_name = 'us-east-1'

#rds settings
rds_endpoint = None
db_username = None
db_password = None
db_name = None


def init_variables():
    session = boto3.session.Session()

    ssm_session = session.client(
        service_name='ssm',
        region_name=region_name
    )
    rds_endpoint = ssm_session.get_parameter(Name=db_endpoint_parameter_name, WithDecryption=True)['Parameter']['Value']
    
    # ------
    
    secrets_session = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    get_secret_value_response = secrets_session.get_secret_value(SecretId=db_secret_name)
    
    secret = ''
    
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    
    json_secrets = json.loads(secret)
    db_username = json_secrets['username']
    db_password = json_secrets['password']

def create_tables():
     """
    This function fetches content from MySQL RDS instance
    """
    try:
        conn = pymysql.connect(rds_endpoint, user=db_username, passwd=db_password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table person_identity (person_id varchar(36) NOT NULL, document_number varchar(15), person_type varchar(1) NOT NULL, PRIMARY KEY (person_id));")
        cur.execute("create table phone (phone_id varchar(36) NOT NULL, phone_number varchar(15), person_id varchar(36), PRIMARY KEY (phone_id), FOREIGN KEY (person_id) REFERENCES person(person_id));")
        cur.execute("create table person (person_id varchar(36) NOT NULL, firstname varchar(255), lastname varchar(255) NOT NULL, PRIMARY KEY (person_id), FOREIGN KEY (person_id) REFERENCES person_identity(person_id));")
        conn.commit()
        cur.execute("select * from person;")
        for row in cur:
            item_count += 1
            logger.info(row)
    conn.commit()

    return "Tables created with %d items" %(item_count)


def lambda_handler(event, context):    
    init_variables()
    create_tables()