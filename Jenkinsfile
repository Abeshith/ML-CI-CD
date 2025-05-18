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

        stage('Lint and Test Code') {
            steps {
                script {
                    echo 'Linting and Testing code...'
		    sh "python3 -m pip install --break-system-packages -r  requiements.txt"
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

