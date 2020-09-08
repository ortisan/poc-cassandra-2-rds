import sys
import logging
import pymysql
import config
#rds settings
rds_host  = config.rds_endpoint
name = config.db_username
password = config.db_password
db_name = config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table person ( id  varchar(36) NOT NULL, firstname varchar(255), lastname varchar(255) NOT NULL, PRIMARY KEY (id))")
        conn.commit()
        cur.execute("select * from person")
        for row in cur:
            item_count += 1
            logger.info(row)
    conn.commit()

    return "Database created with %d items" %(item_count)