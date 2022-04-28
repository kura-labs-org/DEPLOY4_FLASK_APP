pipeline{
    
  agent any
  
  stages{
    
    stage('test2'){
        steps([$class: 'AWSEBDeploymentBuilder', credentialId: 'AWS_CR', applicationName: 'url-shortner', awsRegion: 'us-east-1', bucketName: 'randomname002', environmentName: 'urlshortner-env', 
        keyPrefix: 'python-app', rootObject: '.', versionLabelFormat: '${BUILD_ID}'])
    }
  }
}
