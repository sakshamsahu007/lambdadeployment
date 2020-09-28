import os
from git.repo.base import Repo
import pathlib
import pip

#import zipfile
import shutil
import logging
import boto3
from botocore.exceptions import ClientError
import subprocess


def file_download():

    
    Repo.clone_from("https://github.com/sakshamsahu007/DevOps.git", '../Test')
    
    file = pathlib.Path('../Test/requirements.txt')

    if file.exists():
        print('File exists and installing...')
        pip.main(['install', '-t', '../Test', '-r', '../Test/requirements.txt'])
    else:
        print("File does not exist.")


def create_zip():

    shutil.make_archive('files', 'zip', "H:\\Test" )
    print('zip file created successfully')
    
    
def upload_zipfile_s3(file_name, bucket, object_name=None):

    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        print("started")
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(response)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True 


def upload_to_lambda():

    client=boto3.client('lambda')

    response = client.update_function_code(
        FunctionName='testlambda',
        S3Bucket='sakshamtest',
        S3Key='files.zip',
    )   

    print(response)






file_download()
#create_zip()
#upload_zipfile_s3('H:\\DevOpsAutomation\\files.zip', 'sakshamtest', 'files.zip')
#upload_to_lambda()












