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
                    python3 scripts/update-web-server.py
                    '''
                }
            }
        }
    }
}
