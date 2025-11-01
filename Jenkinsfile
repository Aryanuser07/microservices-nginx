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

        stage('Deploy Containers') {
            steps {
                echo '🚀 Starting containers...'
                bat 'docker-compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo '🔍 Checking running containers...'
                bat 'docker ps'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! All microservices are running.'
        }
        failure {
            echo '❌ Deployment failed. Check Jenkins console output.'
        }
    }
}
