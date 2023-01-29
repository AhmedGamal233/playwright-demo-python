pipeline {
agent any
    environment {
        PATH = "$PATH:/usr/local/bin/"
    }
stages {
    
    stage('e2e-tests') {
        steps {
        withEnv(["PATH=$PATH:~/.local/bin"]){
    
        sh 'docker-compose -f docker-compose.yml run tests'
        }
    }
    }
}
}