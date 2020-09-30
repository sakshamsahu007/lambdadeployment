pipeline {
		agent { node { label "${env.Environment}"}}
		//ToDo select label based on environment variable - DEV QA PROD N2P
		stages{
    
			stage('Download From Repo') {
				steps {
					echo "${env.REPO_URL}"
					bat  "python lambda_deployment.py code_download ${env.REPO_URL} ${env.WORKSPACE} ${env.LAMBDA_FUNCTION_NAME}" //complete path
					
					}
				}
			stage('Install Dependencies') {
				steps {
					bat "python lambda_deployment.py install_depedencies ${env.REPO_URL} ${env.WORKSPACE} ${env.LAMBDA_FUNCTION_NAME}"
					}          
				}
        
			stage('Create Zip') {
				steps {
					bat "python lambda_deployment.py create_zip ${env.REPO_URL} ${env.WORKSPACE} ${env.LAMBDA_FUNCTION_NAME}"
					}
				}
			stage('Upload to S3') {
				steps {
					bat "python lambda_deployment.py upload_zipfile_s3 ${env.REPO_URL} ${env.WORKSPACE} ${env.LAMBDA_FUNCTION_NAME}"
					}
				}
			stage('Upload to Lambda') {
				steps {
					bat "python lambda_deployment.py upload_to_lambda ${env.REPO_URL} ${env.WORKSPACE} ${env.LAMBDA_FUNCTION_NAME}"
					}
				}
		}
}
