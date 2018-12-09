pipeline {
    agent {
        docker {
            image 'python:3.6-alpine'
        }
    }
    stages {
        stage('build') {

            steps {
                sh 'pip3 install --upgrade pip setuptools'
                sh 'apk add --update alpine-sdk make gcc && rm -rf /var/cache/apk/*'
                sh 'pip install -r config/requirements.txt'
            }
        }
        stage('Test') {

            steps {
                sh 'python -m pytest --verbose --junit-xml test-reports/results.xml tests/lab1/utestsLab1.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Static code metrics') {
            steps {
                echo "Code Coverage"
                sh  '''coverage run tests/lab1/utestsLab1.py
                       python -m coverage xml -o ./reports/coverage.xml
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }
    }
}

