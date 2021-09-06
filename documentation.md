# Deployment 4 Flask App

### Objective

Utilizing AWS Elastic Beanstalk and Cloudbees' Jenkins, we want to successfully build a Flask application onto a virtual environment.

### Building the URL Shortener

This process involved the least effort. The app to be deployed was already written for us, and so most of the challenge was correctly configuring our EB environment and Jenkins settings. The EB environemnt is initiliazed by a newly created IAM user - `Jenkins-user`. This account only has AWS EB privileges. I believe this is best practice as it is a more secure approach: there will be a later step that requires us to expose this accounts keys on the Jenkins program, so that it can build onto the EB environment. Should the keys be compromised, at least they don't belong to an account with full admin access.

The Beanstalk environment starts an EC2 instance to host our app, and a second EC2 with Jenkins installed builds it onto the first instance. Jenkins uses two plugins, `Cloudbees Credentials Plugin` and `AWS Elastic Beanstalk`. CCP allows us to use credentials and environment variables
