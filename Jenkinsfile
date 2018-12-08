pipeline {
    agent none
    stages {
        agent {
            docker {
                image 'python:3.6-alpine'
            }
        }
        stage('build') {

            steps {
                sh 'pip3 install --upgrade pip setuptools'
                sh 'pip install -r config/requirements.txt'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml tests/lab1/utestsLab1.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}

