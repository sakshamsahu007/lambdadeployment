pipeline {
		agent { node { label "${env.Environment}"}}
		//agent any
		// parameters{
		// 	choice(
		// 		name: 'Environment',
		// 		choices: 'DEV_SLAVE\nQA_SLAVE',
		// 		description: "Choose Enviroment to build"
		// 	)	
		// }
   
		stages{
    
			stage('Download From Repo') {
				steps {
					echo "${env.REPO_URL}"
					sh "python3 lambda_deployment.py code_download ${env.REPO_URL} ${env.WORKSPACE}" //complete path
					
					}
				}
			stage('Install Dependencies') {
				steps {
					sh "python3 lambda_deployment.py install_depedencies ${env.REPO_URL} ${env.WORKSPACE}"
					}          
				}
        
			stage('Create Zip') {
				steps {
					sh "python3 lambda_deployment.py create_zip ${env.REPO_URL} ${env.WORKSPACE}"
					}
				}
			stage('Upload to S3') {
				steps {
					echo "Uploading to S3...."
					}
				}
			stage('Upload to Lambda') {
				steps {
					echo "Uploading to Lambda...."
					}
				}
		}
}
