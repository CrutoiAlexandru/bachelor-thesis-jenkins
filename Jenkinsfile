final node = 'web-server-ubuntu-agent'
final mgmnt_node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    stages {
        stage('Get rds host') {
            steps {
                agent {
                    label mgmnt_node
                }

                script {
                    sh(script:'python3 scripts/get_rds_host.py', returnStdout: true).trim().eachLine { line ->
                        if (line.startsWith('arn')) {
                            env.RDS_HOST = line
                        }
                    }
                }
            }
        }
        stage('Update web server') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'jenkins-rds-username-password', usernameVariable: 'RDS_USER', passwordVariable: 'RDS_PASSWORD')]) {
                        sh '''
                        pip3 install boto3 mysql-connector-python
                        python3 scripts/update-web-server.py
                        '''
                    }
                }
            }
        }
    }
}
