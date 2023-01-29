pipeline {
agent any
stages {
    stage('e2e-tests') {
        steps {
        sh 'docker-compose run tests'
        }
    }
}
}