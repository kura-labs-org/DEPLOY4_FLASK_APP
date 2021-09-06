# Deployment 4 Flask App

### Objective

Utilizing AWS Elastic Beanstalk and Cloudbees' Jenkins, we want to successfully build a Flask application onto a virtual environment.

### Building the URL Shortener

This process involves the least effort. The app to be deployed is already written for us, and so most of the challenge is to correctly configure our EB environment and Jenkins settings. The EB environemnt is initiliazed by a newly created IAM user - `Jenkins-user`. This account only has AWS EB privileges. I believe this is best practice as it is a more secure approach: there will be a later step that requires us to expose this accounts keys on the Jenkins program, so that it can build onto the EB environment. Should the keys be compromised, at least they don't belong to an account with full admin access.

The EB environment starts an EC2 instance to host our app, and a second EC2 with Jenkins installed builds it onto the first instance. Jenkins uses two plugins, `Cloudbees Credentials Plugin` and `AWS Elastic Beanstalk`. CCP allows us to use credentials and environment variables, while AWSEB plugin allows Jenkins to integrate with our EB environment, done with the aforementioned keys. Once all the information is entered correctly, Jenkins should successfully build the app and by clicking on the environment URL, you can access the site.

### Building the To-Do App

Since the steps are very similar, I will foucs on the fixes implemented.

Firstly, the name of my central `.py` file was labeled `main.py` instead of `application.py`. By following the tutorial, I had named it as such and only realized I needed to change it by re-reading the deployment instructions.

Secondly, in the `application.py` file, I needed to change the line `app = FLASK(__name__)` to `application = FLASK(__name__)`, and all subsequent `@app.route`s to `@application.route`. This information was relayed to me a via a classmate. Though this doesn't seem to make sense since the URL Shortener app utilized "app" instead of "application" and still worked, this one change resulted in Jenkins building the app successfully. 
