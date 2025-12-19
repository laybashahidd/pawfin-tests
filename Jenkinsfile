pipeline {
    agent any
    
    environment {
        APP_URL = 'http://13.60.49.1:4000'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning test repository...'
                git branch: 'main', url: 'https://github.com/laybashahidd/pawfin-tests.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image for Selenium tests...'
                sh 'docker build -t pawfin-selenium-tests .'
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests in Docker container...'
                sh '''
                    docker run --rm \
                        -e APP_URL=${APP_URL} \
                        -v $(pwd):/results \
                        pawfin-selenium-tests \
                        sh -c "python -m pytest test_pawfinds.py -v --tb=short --junitxml=/results/test-results.xml || true"
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker rmi pawfin-selenium-tests || true'
        }
        success {
            emailext (
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build passed! Check: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: '${GIT_AUTHOR_EMAIL}'
            )
        }
        failure {
            emailext (
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed! Check: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: '${GIT_AUTHOR_EMAIL}'
            )
        }
    }
}
