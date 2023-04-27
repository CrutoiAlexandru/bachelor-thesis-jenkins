final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        string(name: 'PRODUCT_NAME')
        string(name: 'BUILD_NUMBER')
    }

    stages {
        stage('Check params') {
            steps {
                script {
                    if (params.PRODUCT_NAME == null || params.PRODUCT_NAME == '') {
                        error('PRODUCT_NAME is not set')
                    }
                    if (params.BUILD_NUMBER == null || params.BUILD_NUMBER == '') {
                        error('BUILD_NUMBER is not set')
                    }
                }
            }
        }
        stage('Set build number') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'jenkins-rds-username-password', usernameVariable: 'RDS_USER', passwordVariable: 'RDS_PASSWORD')]) {
                        sh("""
                        pip3 install boto3 mysql-connector-python
                        python3 scripts/set-build-number.py '${params.PRODUCT_NAME}' '${params.BUILD_NUMBER}'
                        """)
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
