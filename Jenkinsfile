pipeline {
    agent any 
    stages {
        /*stage('Checkout') {
            steps { 
               // bat 'ssh-agent'
                sshagent(credentials: ['github_ssh']) {
                    git branch: 'staging', url: 'git@github.com:TimotheeNourris/MachineLearningInProductionTPJenkins2.git', credentialsId: 'github_ssh'
                    bat 'git branch --delete staging'
                    bat 'git branch staging' 
                    //bat 'git branch -D staging'
                    bat 'git checkout staging'
                    bat 'git push origin staging'
                }
            }
        }*/
        stage('Checkout and staging branch creation') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'http_test', passwordVariable: 'TimoDu91**', usernameVariable: 'timothee.nourris@efrei.net')]) {
                    git url: 'https://github.com/TimotheeNourris/MachineLearningInProductionTPJenkins2.git', credentialsId: 'http_test', branch: 'dev'
                    //bat 'git branch staging' 
                    //bat 'git branch -D staging'
                    //bat 'git checkout dev'
                    //bat 'git push origin staging'
                    bat 'git branch -d staging'
                    bat 'git checkout -b staging'
                    bat 'git push -u origin staging'
                    bat 'git checkout main'
                    //bat 'git merge staging'
                    //bat 'git push origin main'
                }
            }
        }
        stage('Build part') {
            steps {
                bat 'echo build start'
                bat 'pip install -r requirements.txt'
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
                //bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                //bat 'docker push jenkinsdocker'
            }
        }       
    }    
    /*stage('Parallel stages') {
parallel([
{
stage('pushes_git') {
bat 'git checkout staging'
bat 'git push origin --delete main'
bat 'git branch --delete staging'
}
},
{
stage('pushes_docker') {
bat 'docker push timotheenourriscli/jenkins_docker'
}
}
])
}*/
    triggers {
        githubPush()
    }
}
