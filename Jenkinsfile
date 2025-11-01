pipeline {
    agent any

    environment {
        DOCKER_USER = 'aryan0763'
        DOCKER_PASS = credentials('dockerhub-creds')   // ✅ Fixed ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📦 Pulling latest code..."
                git branch: 'main', url: 'https://github.com/Aryanuser07/microservices-nginx.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "🐳 Building Docker images..."
                bat 'docker-compose build'
            }
        }

        stage('Clean Old Containers') {
            steps {
                echo "🧹 Cleaning old containers..."
                bat '''
                echo Stopping and removing existing containers if any...
                docker-compose down --remove-orphans || exit 0
                docker rm -f user-service order-service product-service nginx-reverse-proxy 2>nul || exit 0
                '''
            }
        }

        stage('Deploy Containers') {
            steps {
                echo "🚀 Deploying new containers..."
                bat 'docker-compose up -d'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "📤 Pushing images to DockerHub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker tag microservices-nginx-pipeline-user-service %DOCKER_USER%/microservices-nginx-user-service:latest
                    docker tag microservices-nginx-pipeline-product-service %DOCKER_USER%/microservices-nginx-product-service:latest
                    docker tag microservices-nginx-pipeline-order-service %DOCKER_USER%/microservices-nginx-order-service:latest
                    docker push %DOCKER_USER%/microservices-nginx-user-service:latest
                    docker push %DOCKER_USER%/microservices-nginx-product-service:latest
                    docker push %DOCKER_USER%/microservices-nginx-order-service:latest
                    '''
                }
            }
        }
    }
}
