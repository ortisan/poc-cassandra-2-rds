import boto3
from datetime import date

if __name__ == "__main__":
    bucket_name = 'ortiz-cassandra-backups-' + date.today().strftime("%Y-%m-%d")
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket=bucket_name)
    s3.meta.client.upload_file("data/person-out.csv", bucket_name, 'person_backup.csv')