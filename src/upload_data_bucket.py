import glob
from datetime import date
import boto3
import os
import multiprocessing as mp
from multiprocessing.pool import Pool, ThreadPool
import threading
import time

BUCKET_NAME = 'data-ortiz-2020'

s3 = boto3.resource('s3')

def upload_file(file, **kwargs):
    try:
        filename = os.path.basename(file)
        s3.meta.client.upload_file(file, BUCKET_NAME, filename)
        return (filename, True)
    except Exception as err:
        return (filename, False)

if __name__ == "__main__":
    with ThreadPool(mp.cpu_count()) as pool:    
        results = pool.map(upload_file, glob.glob("data/person-out.csv"))
        print(results)
