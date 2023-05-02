final node = 'web-server-ubuntu-agent'

pipeline {
    agent {
        label node
    }

    stages {
        stage('Host web server') {
            steps {
                script {
                    sh '''
                    pip3 install -r boto3 mysql-connector-python
                    python3 scripts/update-web-server.py
                    '''
                }
            }
        }
    }
}
