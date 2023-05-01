final node = 'cicd-ubuntu-agent'

pipeline {
    agent {
        label node
    }

    stages {
        stage('Execute build') {
            steps {
                script {
                    sh('''
                    cd Docker
                    sudo docker build -t flask-file-hosting .
                    ''')
                }
            }
        }

        stage('Get build number') {
            steps {
                script {
                    def build = build(
                        job: 'utility/get-build-number',
                        parameters: [booleanParam(name: 'INCREMENT', value: 'True')])
                    env.BUILD_NUMBER = build.getBuildVariables()['BUILD_NUMBER']
                }
            }
        }

        stage('Push image to DockerHub') {
            steps {
                script {
                    def dockerHubRepo = 'crutoialexandru/flask-file-hosting'
                    def productName = 'flask-file-hosting'
                    sh("""
                    sudo docker tag ${productName}:${env.BUILD_NUMBER} ${dockerHubRepo}:${env.BUILD_NUMBER}
                    sudo docker push ${dockerHubRepo}:${env.BUILD_NUMBER}
                    sudo docker system prune -a -f
                    """)
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
