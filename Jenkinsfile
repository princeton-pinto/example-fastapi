pipeline {
  agent any
  stages {
    stage('Checkout code') {
      steps {
        git(url: 'https://github.com/princeton-pinto/example-fastapi.git', branch: 'main')
      }
    }

    stage('Add a log') {
      steps {
        sh 'ls -la'
      }
    }

  }
}