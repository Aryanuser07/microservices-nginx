pipeline {
    agent any

    environment {
        COMPOSE_CMD = 'docker-compose'
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
                bat "${COMPOSE_CMD} build"
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
                bat "${COMPOSE_CMD} up -d"
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '📤 Pushing images to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat '''
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker tag microservices-nginx-user-service %DOCKER_USER%/microservices-nginx-user-service:latest
                    docker tag microservices-nginx-product-service %DOCKER_USER%/microservices-nginx-product-service:latest
                    docker tag microservices-nginx-order-service %DOCKER_USER%/microservices-nginx-order-service:latest

                    docker push %DOCKER_USER%/microservices-nginx-user-service:latest
                    docker push %DOCKER_USER%/microservices-nginx-product-service:latest
                    docker push %DOCKER_USER%/microservices-nginx-order-service:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! All microservices are up and running.'
        }
        failure {
            echo '❌ Deployment failed. Check logs for details.'
        }
    }
}
