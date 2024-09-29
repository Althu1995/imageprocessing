"""config file for get status pytest"""
import os
import boto3


class Data:
    """Class where resources required and
    inputs required for pytest is defined"""
    def __init__(self):
        os.environ["logging_level"] = "debug"
        os.environ["image_bucket_name"] = "test_bucket"
        os.environ["image_path"] = "upload_dowload_image/images/"

    def _setup_resources_with_companycode_from_jwt(self):
        self.event = {
            "imageName": "happy",
            "operation": "upload"
        }
        s3 = boto3.client('s3', region_name="us-east-1")
        s3.create_bucket(Bucket='test-bucket')
        self.event['s3_client'] = s3

    def _setup_resources_with_companycode_from_payload(self):
        self.event = {
            "thumbnailName": "happy",
            "operation": "download"
        }
        s3 = boto3.client('s3', region_name="us-east-1")
        s3.create_bucket(Bucket='test-bucket')
        s3.upload_file(
            "upload_dowload_image/images/happy.jpg", 'test-bucket',
            'thumbnail/happy.jpg')
        self.event['s3_client'] = s3
