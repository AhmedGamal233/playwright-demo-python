pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin/"
}
stages {
    stage('Checkout') {
    steps {
        script {
        cleanWs()
          // The below will clone your repo and will be checked out to master branch by default.
        git credentialsId: 'jenkins-user-github', url: 'https://github.com/AhmedGamal233/playwright-demo-python.git'
          // Do a ls -lart to view all the files are cloned. It will be clonned. This is just for you to be sure about it.
        sh "ls -lart ./*"
          // List all branches in your repo. 
        sh "git branch -a"
          // Checkout to a specific branch in your repo.
        sh "git checkout master"
        }
    }
    }
    stage('changeBrowser') {
    steps {
        script {
        //you need to install content replacement plugin https://plugins.jenkins.io/content-replace/#plugin-content-pipeline-job-configuration
        contentReplace(configs: [fileContentReplaceConfig(configs: [fileContentReplaceItemConfig(matchCount: 1, replace: '${BrowserName}', search: '(?<=browserName =).*')], fileEncoding: 'UTF-8', filePath: 'pytest.ini')])
        }
    }
    }
    stage('e2e-tests') {
    steps {
        withEnv(["PATH=$PATH:~/.local/bin"]) {
        sh 'docker-compose -f docker-compose.yml run tests'
        }
    }
    }
}
}