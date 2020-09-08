import glob
from datetime import date
import boto3
import os
import multiprocessing as mp
from multiprocessing.pool import Pool, ThreadPool
import threading
import time

bucket_name = 'ortiz-cassandra-backups-' + date.today().strftime("%Y-%m-%d")

s3 = boto3.resource('s3')

def create_bucket():
    s3.create_bucket(Bucket=bucket_name)

def upload_file(file, **kwargs):
    try:
        filename = os.path.basename(file)
        s3.meta.client.upload_file(file, bucket_name, filename)
        return (filename, True)
    except Exception as err:
        return (filename, False)

if __name__ == "__main__":
    with ThreadPool(mp.cpu_count()) as pool:    
        results = pool.map(upload_file, glob.glob("data/split_person*"))
        print(results)
