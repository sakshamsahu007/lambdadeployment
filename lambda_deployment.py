import os
from git.repo.base import Repo
import pathlib
import pip

import zipfile
import shutil
import logging
import boto3
from botocore.exceptions import ClientError
#import subprocess

import sys

if( len(sys.argv) < 4):
    print("Insufficient Arguments.")
    exit(1)
    

mode=sys.argv[1]
repo=sys.argv[2]
workspace=sys.argv[3]
lambda_function_name=sys.argv[4]
code_directory=workspace + '/code'
s3_bucket_name='sakshamtest'
s3_object_name='code.zip'
code_zip_file_path= code_directory + '.zip'

def code_download(repo, workspace):
    print(repo)
    
    if (os.path.isdir(code_directory)):
        shutil.rmtree(code_directory)

    Repo.clone_from(repo, code_directory) 
    #ToDo fetch and checkout based on Environment Varaiable


def install_depedencies(workspace):
    
    file = pathlib.Path(code_directory + '/requirements.txt')

    if file.exists():
        print('Installing modules...')
        pip.main(['install', '-t', code_directory, '-r', code_directory + '/requirements.txt'])
    else:
        print("File does not exist.")
        exit(1)


def create_zip(workspace):
    shutil.make_archive('code', 'zip', workspace + '/code')
    print('zip file created successfull y')


def upload_zipfile_s3(file_path, s3_bucket_name, s3_object_name):
    s3_client = boto3.client('s3')
    try:
        print("file upload started")
        response = s3_client.upload_file(file_path, s3_bucket_name, s3_object_name)
        print(response)
        print("file upload complete")
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


#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#print (sys.argv[1])


if (mode == 'code_download'):
    code_download(repo, workspace)
elif (mode == 'install_depedencies'):
    #install_depedencies(workspace)
    print("Dummy Installation completed...")
elif (mode == 'create_zip'):
    create_zip(workspace)
elif (mode == 'upload_s3'):
    upload_zipfile_s3(code_zip_file_path,s3_bucket_name,s3_object_name)

#file_download()
#create_zip()
#upload_zipfile_s3('H:\\DevOpsAutomation\\files.zip', 'sakshamtest', 'files.zip')
#upload_to_lambda()