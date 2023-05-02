final node = 'web-server-ubuntu-agent'

pipeline {
    agent {
        label node
    }

    stages {
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
