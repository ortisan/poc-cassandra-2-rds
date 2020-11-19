import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

import json
def parse_phone_json(array_str):
    json_obj = json.loads(array_str)
    for item in json_obj:
       yield (item["id"], item["phone_number"])
       
       
# Define the schema
from pyspark.sql.types import ArrayType, IntegerType, StringType, StructType, StructField
phone_json_schema = ArrayType(StructType([StructField('id', StringType(), nullable=False), StructField('phone_number', IntegerType(), nullable=False)]))

# Define udf
from pyspark.sql.functions import udf
udf_phone_parse_json = udf(lambda str: parse_phone_json(str), phone_json_schema)

def map_phone(rec):
    rec["phones"] = udf_phone_parse_json(rec.phones)
    return rec

# Job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# sc = SparkContext()
# glueContext = GlueContext(sc)
# spark = glueContext.spark_session
# job = Job(glueContext)
# job.init(args['JOB_NAME'], args)
glueContext = GlueContext(SparkContext.getOrCreate())

datasource_migration = glueContext.create_dynamic_frame.from_catalog(database="gluemigrationdb", table_name="data_ortiz_2020", transformation_ctx="datasource_migration")

# Separating Phone from DF
splited_databases = SplitFields.apply(datasource_migration,['id', 'phones'], name1="phones_df", name2="rest_df")
phones_df = splited_databases.select("phones_df")

phones_mapped_df = Map.apply(frame = phones_df, f = map_phone)
phones_mapped_df.printSchema()


# phones_df.select("id").show()

# Generate a new data frame with the expected schema
# phones_df_new = phones_df.select(phones_df.id, udf_phone_parse_json(phones_df.phones).alias("phones"))
# phones_df_new.show()
# phones_df_new.printSchema()

print("End")


#datasource_migration.drop_fields(['phones'])
#datasource_migration.printSchema()