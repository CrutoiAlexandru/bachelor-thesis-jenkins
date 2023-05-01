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
                    sudo docker build --no-cache -t flask-file-hosting .
                    ''')
                }
            }
        }

        stage('Get build number') {
            steps {
                script {
                    def build = build(
                        job: 'utility/utility-get-build-number',
                        parameters: [
                            string(name: 'PRODUCT_NAME', value: 'FlaskFileHosting'),
                            booleanParam(name: 'INCREMENT', value: 'True')])
                    env.BUILD_NUMBER = build.getBuildVariables()['BUILD_NUMBER']
                    if (env.BUILD_NUMBER == null || env.BUILD_NUMBER == '' || env.BUILD_NUMBER == 'null') {
                        error('Build number is null')
                    }
                    println("Build number: ${env.BUILD_NUMBER}")
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
