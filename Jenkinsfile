pipeline {
    agent any

    environment {
        // Define environment variables here
        DOCKERHUB_CREDENTIAL_ID = 'mlops-jenkins-dockerhub-token'
        DOCKERHUB_REGISTRY = 'https://registry.hub.docker.com'
        DOCKERHUB_REPOSITORY = 'iquantc/mlops-proj-01'
	PATH = "${env.HOME}/.local/bin:${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building Docker image...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'mlops-git',
                            url: 'https://github.com/Abeshith/ML-CI-CD.git'
                        ]]
                    )
                }
            }
        }

        stage('Lint Code') {
            steps {
                script {
                    echo 'Linting code...'
		     echo 'Linting code...'
            	     sh "python3 -m pip install --break-system-packages -r requirements.txt"
          	     sh "which pylint || echo 'pylint not found in PATH'"
           	     sh "pylint app.py train.py --output=pylint-report.txt --exit-zero || true"
                     sh "flake8 app.py train.py --ignore=E501,E302 --output-file=flake8-report.txt || true"
           	     sh "black app.py train.py || true"
                }
            }
        }

	stage('Test Code') {
            steps {
                script {
                    echo 'Testing code...'
                    sh "pytest tests/"
                }
            }
        }

        stage('Trivy FS Scan') {
            steps {
                script {
                    echo 'Running Trivy FS scan...'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                }
            }
        }

        stage('Trivy Image Scan') {
            steps {
                script {
                    echo 'Running Trivy image scan...'
	            sh "trivy fs ./ --format table -o trivy-fs-report.html"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
		    docker.build("mlops-app")
                }
            }
        }
	stage('Scan Docker image with Trivy') {
            steps {
                script {
                    echo 'Scanning Docker Image with Trivy...'
		    sh 'trivy image mlops-app:latest --format table -o trivy-image-report.html'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                }
            }
        }
    }
}

