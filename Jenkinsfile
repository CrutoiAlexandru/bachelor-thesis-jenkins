final node = 'web-server-ubuntu-agent'

pipeline {
    agent {
        label node
    }

    stages {
        stage('Update web server') {
            steps {
                script {
                    sh '''
                    pip3 install boto3 mysql-connector-python
                    python3 scripts/update-web-server.py
                    '''
                }
            }
        }
    }
}
