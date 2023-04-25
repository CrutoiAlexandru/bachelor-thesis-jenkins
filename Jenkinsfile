final node = 'cicd-ubuntu'

pipeline {
    agent {
        label node
    }

    stages {
        stage('Execute build') {
            steps {
                script {
                    sh('''
                    sudo apt update
                    sudo apt install -y python3-pip
                    pip3 install -r requirements.txt
                    python3 src/main.py
                    ''')
                }
            }
        }

        stage('Clean WS') {
            steps {
                cleanWs()
            }
        }
    }
}
