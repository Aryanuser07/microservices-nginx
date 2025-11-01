pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
        COMPOSE_DOCKER_CLI_BUILD = '1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Pulling latest code...'
                git branch: 'main', url: 'https://github.com/Aryanuser07/microservices-nginx.git'
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
                docker rm -f user-service order-service product-service nginx-reverse-proxy 2>nul || exit 0
                '''
            }
        }

        stage('Deploy Containers') {
            steps {
                echo '🚀 Deploying new containers...'
                bat 'docker-compose up -d'
            }
        }

        // Optional: Add this stage later after verifying successful deploy
        /*
        stage('Verify Services') {
            steps {
                echo '🔍 Checking service health...'
                bat '''
                curl -s http://localhost/users
                curl -s http://localhost/products
                curl -s http://localhost/orders
                '''
            }
        }
        */
    }

    post {
        success {
            echo '✅ Deployment successful! All microservices are up and running.'
        }
        failure {
            echo '❌ Deployment failed. Check Jenkins console output for details.'
        }
    }
}
