

import sys
import re
import json
from pyspark.context import SparkContext
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, IntegerType, StringType, StructType, StructField

from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.transforms import *

def parse_phone_json(array_str):
    """ 
    Transform String into Json and extract id and Phone Number
    input: array_str: json of phones
    """
    # Include commas for UDT cassandra
    json_str = re.sub(r'([a-zA-Z0-9_]+)\s*:\s*([^,}]+)?', '"\\1": "\\2"', x)
    # Replace double commas
    json_str = re.sub(r'(\"\')|(\'\")', '"', json_str)    
    json_obj = json.loads(json_str)
    for item in json_obj:
        # Extracts id and phone number
        yield (item["id"], item["phone_number"])

glueContext = GlueContext(SparkContext.getOrCreate())

try:
    spark = glueContext.spark_session
    
    # Read data from glue database
    datasource_migration = glueContext.create_dynamic_frame.from_catalog(database = "person_db", table_name = "data_ortiz_2020", transformation_ctx = "datasource_migration")
    
    # Define the phone schema
    phone_json_schema = ArrayType(StructType([StructField('id', StringType(), nullable=False), StructField('phone_number', IntegerType(), nullable=False)]))

    # Define udf
    udf_phone_parse_json = udf(lambda json_str: parse_phone_json(json_str), phone_json_schema)
    
    # Separating Phone from DF
    splited_databases = SplitFields.apply(datasource_migration,['id', 'phones'], name1="phones_df", name2="rest_df")
    
    phones_df = splited_databases.select("phones_df").toDF()
    phones_df = phones_df.select(phones_df.id, udf_phone_parse_json(phones_df.phones).alias("phones"))

    phones_df.show()
    phones_df.printSchema()

    # TODO DATABASE INSERT
    
except Exception as exc:
    ## TODO EXCEPTION HANDLER
    print(exc)
