final node = 'aws-mgmnt-agent'

pipeline {
    agent {
        label node
    }

    parameters {
        choice(
            name: 'ACTION',
            choices: ['shutdown', 'startup', 'total-shutdown'],
            description: '''
            Action to perform <br>
            <ul>
                <li>shutdown: shutdown one instance</li>
                <li>startup: startup one instance</li>
                <li>total_shutdown: shutdown all the instances on the AWS server</li>
            </ul>
            ''',
        )
        string(
            name: 'INSTANCE_NAME',
            description: '''
            Name of the instance you want to apply the action to. <br>
            Used only for shutdown and startup. <br>
            If not provided, the action will not work.
            '''
        )
    }

    stages {
        stage('Check parameters') {
            steps {
                script {
                    if (params.ACTION == 'shutdown' || params.ACTION == 'startup') {
                        if (params.INSTANCE_NAME == '') {
                            error('INSTANCE_NAME is required for shutdown and startup')
                        }
                    }
                }
            }
        }

        stage('Checkout') {
            steps {
                git(
                    credentialsId: 'jenkins-github-credentials',
                    url: 'https://github.com/CrutoiAlexandru/bachelor-thesis-jenkins.git',
                    branch: env.BRANCH_NAME
                )
            }
        }

        stage('Execute script') {
            steps {
                script {
                    sh("""
                    chmod +x ./scripts/${params.ACTION}.py
                    python3 ./scripts/${params.ACTION}.py
                    """)
                }
            }
        }
    }
}
