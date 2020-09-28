pipeline {
		agent { node { label 'DEV_SLAVE'}}
   
		stages{
    
			stage('Download') {
				steps {
					echo "Downloading...."
					}
				}
			stage('Install from requirements.txt') {
				steps {
					echo "Installing...."
					}          
				}
        
			stage('Create Zip') {
				steps {
					echo "Creating Zip...."
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
