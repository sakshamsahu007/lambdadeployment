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

def code_download(repo, workspace):
    print(repo)
    code_directory=workspace + '/code'
    if( os.path.isdir(code_directory)):
        shutil.rmtree(code_directory)

    Repo.clone_from(repo, code_directory) 
    #ToDo fetch and checkout based on Environment Varaiable

def install_depedencies(workspace):
    code_directory=workspace + '/code'
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


#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
#print (sys.argv[1])


if (mode == 'code_download'):
    code_download(repo, workspace)
elif (mode == 'install_depedencies'):
    install_depedencies(workspace)
elif (mode == 'create_zip'):
    create_zip(workspace)

#file_download()
#create_zip()
#upload_zipfile_s3('H:\\DevOpsAutomation\\files.zip', 'sakshamtest', 'files.zip')
#upload_to_lambda()