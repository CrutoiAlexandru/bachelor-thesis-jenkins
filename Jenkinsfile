final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        string(
            name: 'INSTANCE_NAME',
            description: '''
            Name of the instance you want to update the credentials on. <br>
            If not provided, the action will not work.
            '''
        )
    }

    stages {
        stage('Check parameters') {
            steps {
                script {
                    if (params.INSTANCE_NAME == '') {
                        error('INSTANCE_NAME is required')
                    }
                }
            }
        }

        stage('Execute script') {
            steps {
                script {
                    sh("""
                    chmod +x ./scripts/update-credentials.sh
                    ./scripts/update-credentials.sh ${params.INSTANCE_NAME}
                    """)
                }
            }
        }
    }
}
