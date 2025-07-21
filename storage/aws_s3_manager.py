import boto3

class S3Manager:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_path, s3_key):
        self.s3.upload_file(file_path, self.bucket_name, s3_key)
        print(f"Uploaded {file_path} to s3://{self.bucket_name}/{s3_key}")
