"""
Upload generated content to Amazon S3 using Boto3.
"""

import boto3

def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
