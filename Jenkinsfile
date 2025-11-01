pipeline {
    agent any

    environment {
        REPO = 'Aryanuser07/microservices-nginx'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Pulling latest code...'
                git branch: 'main', url: "https://github.com/${REPO}.git"
            }
        }

        stage('Build Docker Images') {
            steps {
                echo '🐳 Building Docker images...'
                bat 'docker-compose build'
            }
        }

        stage('Clean Old Containers') {
            steps {
                echo '🧹 Cleaning old containers...'
                bat '''
                echo Stopping and removing existing containers if any...
                docker-compose down --remove-orphans || exit 0
                docker rm -f user-service order-service product-service 2>nul || exit 0
                '''
            }
        }

        stage('Deploy Containers') {
            steps {
                echo '🚀 Deploying new containers...'
                bat 'docker-compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo '🔍 Verifying running containers...'
                bat 'docker ps'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! All microservices are running and accessible via Nginx.'
        }
        failure {
            echo '❌ Deployment failed. Check Jenkins console output for details.'
        }
    }
}
