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
                    docker run -d -p 80:80 --name web-server nginx
                    '''
                }
            }
        }
    }
}
