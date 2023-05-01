final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        choice(name: 'PRODUCT_NAME', choices: ['FlaskFileHosting'])
        string(name: 'BUILD_NUMBER')
        choice(name: 'TAG', choices: ['unstable', 'stable'])
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
                    if (params.TAG == null || params.TAG == '') {
                        error('TAG is not set')
                    }
                }
            }
        }
        stage('Set build tag') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'jenkins-rds-username-password', usernameVariable: 'RDS_USER', passwordVariable: 'RDS_PASSWORD')]) {
                        sh("""
                        pip3 install boto3 mysql-connector-python
                        python3 scripts/set-build-tag.py '${params.PRODUCT_NAME}' '${params.BUILD_NUMBER}' '${params.TAG}'
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
