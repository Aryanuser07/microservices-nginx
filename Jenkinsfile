pipeline {
    agent any

    environment {
        PROJECT_DIR = 'microservices-nginx'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Pulling latest code...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo '🐳 Building Docker images...'
                sh 'docker compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                echo '🚀 Deploying all services...'
                sh 'docker compose down --remove-orphans'
                sh 'docker compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo '✅ Checking running containers...'
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo '🎉 Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed. Check logs in Jenkins console.'
        }
    }
}
