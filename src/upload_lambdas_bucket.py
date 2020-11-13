import glob
from datetime import date
import boto3
import os
import multiprocessing as mp
from multiprocessing.pool import Pool, ThreadPool
import threading
import time

bucket_name = 'ortiz-lambdas'

s3 = boto3.resource('s3')

def create_bucket():
    s3.create_bucket(Bucket=bucket_name)

def upload_file(file):
    try:
        filename = os.path.basename(file)
        s3.meta.client.upload_file(file, bucket_name, filename)
        return (filename, True)
    except Exception as err:
        return (filename, False)

if __name__ == "__main__":
    
    create_bucket()
    upload_file('aws/lambdas/create_tables/create_tables.zip')
