pipeline {
    agent any

    stages {
        stage('CLone Git') {
            steps {
                git 'https://github.com/gauravtirodkar/Jenkins.git'
            }
        }
        stage('Build Code'){
            steps{
                sh "chmod u+x Prog1.py"
                sh "./Prog1.py"
            }
        }
        stage('Test Code'){
            steps{
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    }
}
