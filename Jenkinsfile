pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'your_dockerhub_username'   // replace
        PROJECT_NAME = 'microservices-nginx'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Fetching latest code from GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images for all services...'
                bat 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                echo 'Starting containers...'
                bat 'docker-compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo 'Verifying all microservices...'
                bat '''
                curl http://localhost/api/users/
                curl http://localhost/api/products/
                curl http://localhost/api/orders/
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing images to DockerHub...'
                bat """
                docker tag ${PROJECT_NAME}-user-service ${DOCKERHUB_USER}/${PROJECT_NAME}-user-service:latest
                docker tag ${PROJECT_NAME}-product-service ${DOCKERHUB_USER}/${PROJECT_NAME}-product-service:latest
                docker tag ${PROJECT_NAME}-order-service ${DOCKERHUB_USER}/${PROJECT_NAME}-order-service:latest

                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-user-service:latest
                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-product-service:latest
                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-order-service:latest
                """
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Stopping containers...'
                bat 'docker-compose down'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
        success {
            echo '✅ Build successful.'
        }
    }
}
