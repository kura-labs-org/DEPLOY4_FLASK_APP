# DEPLOY04_FLASK_APP

<h1 align=center>Deployment 4</h1>

Welcome to deployment 4, for this deployment you will need to deploy a Flask application to AWS Elastic Beanstalk. This repository already has a flask app you can deploy to test your setup configurations. Deploy the url shortner application into your AWSEB. After you've deployed the url shortner application, create your own Flask application. Deploy your created flask application and the To Do List application into your AWSEB.    

- Remember to create a requirements.txt for your Flask application and name your application file ***application.py***
- You will have to make three project folders on Jenkins for your three different build projects. 

***Requirements:*** 
- [x]Fork this repo (https://github.com/kura-labs-org/DEPLOY04_FLASK_APP) to have a copy of the url shortner application.
- [x]Create a gitignore file or remove this README.md and Deployment4.pdf instructions from your forked repo before you start your build.
- [x]Take a screenshot of the url shortner home page and add the screenshot to your screenshot file.
- [x]You should have 3 different repositories for the 3 different applications. 
- [x]Create your own Flask application and create a GitHub repository for it.
- [x]Create your GitHub repository for your to do list application.
- [x]Screenshot your deployed Flask application home page and your To Do List application. Then add the screenshot to your screenshot file.   
- [x]Initiate a pull request to the kura-labs-org/DEPLOY4_FLASK_APP with your screenshot file.   

👉Link to deployment instructions: [here](https://github.com/kura-labs-org/DEPLOY4_FLASK_APP/blob/main/Deployment%204.pdf)  

<h1 align=center>Deployment 4 Documentation</h1>
Purpose of first challenge is to the app that was default to this git fork. This application is used to shorten URLs. For this app, we used Jenkins to build a pipeline to manage the build, while connecting github repo and AWS ELB to build the actual application and for deployment.
-Jenkins was set using default settings specified in instructions, with ELB as default as well. The build was successful, though there were some failures as a result of:
-Github account connection to Jenkins servers failing as a result of expired credentials.
-ELB would continue to fail over and over again without much detail on where it went wrong unless Jenkins outputs were looked at.

After correcting for the Git and configurations on Jenkins, the operations went smoothly and a deployment was possible.


<h1 align=center>Deployment 4 Dogbite App</h1>
The purpose of this deployment was to deploy your own app on the ELB using all the information and classwork projects. My app utilized a python script with requests library to pull json data from NYC OPEN Data project, then run the data through functions to create a sorted data of dog bites based on location and gender. This data would then be deployed onto server/app using Flask and ELB for hosting.

Currently, the data functions are working properly, however, there is issue with attempting to print out the data on to the flask subdirectory pages.


I've made past attempted to utilized sqlite3 and import the data, but that was met with a lot of difficulties, so I am pulling data live from the database in realtime and processing during deployment. I also ran into a lot of issues in VScode with Pylance not being able to import the modules, so I had to spend 3 days troubleshooting this issue, including reinstalling interpreters, changing Environment paths, and settting up virutal environments and switching IDEs until I nuked my entire development environment.
