final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        choice(name: 'PRODUCT_NAME', choices: ['FlaskFileHosting'])
        booleanParam(name: 'INCREMENT', defaultValue: false)
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
        stage('Get build number') {
            steps {
                script {
                    def buildNumber = null
                    withCredentials([usernamePassword(credentialsId: 'jenkins-rds-username-password', usernameVariable: 'RDS_USER', passwordVariable: 'RDS_PASSWORD')]) {
                        sh('''
                        pip3 install boto3 mysql-connector-python
                        ''')
                        buildNumber = sh(script: "python3 scripts/get-build-number.py '${params.PRODUCT_NAME}' '${params.INCREMENT}'", returnStdout: true).trim()
                    }
                    env.BUILD_NUMBER = buildNumber
                    echo env.BUILD_NUMBER
                }
            }
        }
    }
}
