pipeline {
    agent any 
    stages {
        stage('Checkout and staging branch creation') {
            steps {
                    //bat 'git branch staging' 
                    bat 'git branch -D staging'
                    //bat 'git checkout dev'
                    //bat 'git push origin staging'
                    //bat 'git branch -d staging'
                    bat 'git checkout -b staging'
                    bat 'git push -u origin staging'
                    bat 'git checkout main'
                    bat 'git merge staging'
                    bat 'git pull origin main'
                    bat 'git push origin main'
                }
        }
        stage('Build part') {
            steps {
                bat 'echo build start'
                bat 'pip3 install -r requirements.txt'
            }
        }
        stage('Test part') {
            steps {       
                bat 'echo test start'
                bat 'python -m unittest'
            }
        }
        stage('Deploy part') {
            steps {
                bat 'docker build -t jenkinsdocker .'
                bat 'docker run -d -p 5000:5000 jenkinsdocker'
                bat 'docker login -u timotheenourriscli -p dckr_pat_liPCBB7KmZ3x_UHNbz9oyMTNpiE'
                bat 'docker tag jenkinsdocker timotheenourriscli/jenkins_docker'
                bat 'docker push timotheenourriscli/jenkins_docker'

            }
        }       
    }    
    triggers {
        githubPush()
    }
}
