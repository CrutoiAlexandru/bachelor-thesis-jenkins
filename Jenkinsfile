final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        choice(name: 'PRODUCT_NAME', choices: ['FlaskFileHosting'])
    }

    stages {
        stage('Check params') {
            steps {
                script {
                    if (params.PRODUCT_NAME == null || params.PRODUCT_NAME == '') {
                        error('PRODUCT_NAME is not set')
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
                        python3 scripts/get-build-number.py '${params.PRODUCT_NAME}'
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
