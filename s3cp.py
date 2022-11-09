import logging
import boto3
import os
import pytest
from moto import mock_s3
from botocore.exceptions import ClientError

def file_to_cloud(fname, bname, prefix):
	s3 = boto3.Session().client('s3')
	with open(fname, "rb") as f:
	    object_name = os.path.basename(f.name)
	    s3.upload_fileobj(f, bname, f"{prefix}/{object_name}")
	
	return True

@mock_s3
def test_file_to_cloud(fname, bname, prefix):
	client = boto3.client('s3', region_name="us-east-1")
	client.create_bucket(Bucket='mybucket')
	file_to_cloud("hello.moto", "mybucket", 'test')
	
	return True
	

