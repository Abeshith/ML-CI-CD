pipeline {
    agent any

    environment {
        // Define environment variables here
        DOCKERHUB_CREDENTIAL_ID = 'mlops-jenkins-dockerhub-token'
        DOCKERHUB_REGISTRY = 'https://registry.hub.docker.com'
        DOCKERHUB_REPOSITORY = 'iquantc/mlops-proj-01'
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
		    sh "python3 -m pip install --break-system-packages -r  requirements.txt"
		    sh "pylint app.py train.py --output=pylint-report.txt --exit-zero"
                    sh "flake8 app.py train.py --ignore=E501,E302 --output-file=flake8-report.txt"
                    sh "black app.py train.py"
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
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
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

