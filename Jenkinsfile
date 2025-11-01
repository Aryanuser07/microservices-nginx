pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'your_dockerhub_username'   // 🔹 replace this
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
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                echo 'Starting all services using docker-compose...'
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo 'Checking if all services are running properly...'
                sh '''
                echo "Testing User Service:" && curl -f http://localhost/api/users/ || exit 1
                echo "Testing Product Service:" && curl -f http://localhost/api/products/ || exit 1
                echo "Testing Order Service:" && curl -f http://localhost/api/orders/ || exit 1
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing images to DockerHub...'
                sh '''
                docker tag ${PROJECT_NAME}-user-service ${DOCKERHUB_USER}/${PROJECT_NAME}-user-service:latest
                docker tag ${PROJECT_NAME}-product-service ${DOCKERHUB_USER}/${PROJECT_NAME}-product-service:latest
                docker tag ${PROJECT_NAME}-order-service ${DOCKERHUB_USER}/${PROJECT_NAME}-order-service:latest

                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-user-service:latest
                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-product-service:latest
                docker push ${DOCKERHUB_USER}/${PROJECT_NAME}-order-service:latest
                '''
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Stopping and removing containers...'
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
        failure {
            echo '❌ Something went wrong in the pipeline.'
        }
        success {
            echo '✅ All stages completed successfully.'
        }
    }
}
