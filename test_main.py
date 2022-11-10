import logging
import os
import s3cp


def test_mock():
	with open("hello.moto", "rb") as f:
	    object_name = os.path.basename(f.name)
	exception_or_True = s3cp.test_file_to_cloud("hello.moto", "mybucket", 
	"test")
	print(f"Upload Successful: {exception_or_True}")

