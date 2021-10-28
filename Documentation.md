# Need to add 2 more screenshots did not find them will have to deploy again.
# Deployment 4
## Aim: To deploy 3 different applications using AWS's elastic beanstalk using jenkins to build them and github to store our code.
## My 3 apps are URL shortener: Flask, todo-list: Flask, Blog-app: React.
# Url Shortener:
![Screenshot 2021-08-28 141211](https://user-images.githubusercontent.com/60336145/135954294-10d6bc5b-23e2-45e8-a0fd-3a4cca8e8167.png)
# Todo-list-app
![Screenshot 2021-10-26 121517](https://user-images.githubusercontent.com/60336145/138937744-e7558030-aaeb-4507-9736-19b9653ea8a6.png)
# Blog-app
![dep4-app](https://user-images.githubusercontent.com/60336145/138937760-84958846-3097-46f4-87ef-f00f550c63e2.png)
# Steps:
# 1. Create an Elastic BeanStalk instance that contains the environment needed for your applicatoin to run EX: Flask uses python, React uses Node.js
# Click on the create environment button to get started.
![image](https://user-images.githubusercontent.com/60336145/139178668-1a49ff8c-77a8-48e0-8aa3-7cdc80a6c5d7.png)
# Select Web server environment option then click on select 
![image](https://user-images.githubusercontent.com/60336145/139178705-2606eb53-7f37-4c80-9528-0a4597b15789.png)
# Choose a name for your application, the Environemnt name will be auto-generated from the name you chose.  Write down your environment or copy it somewhere for later use. you can give a description if you'd like but its not necessary.
![image](https://user-images.githubusercontent.com/60336145/139179142-209005eb-326b-45d1-8bb5-94d91332786b.png)
# choose Managed platform.  Click on the the Platform field to see a dropdown menu with a list of options.
![image](https://user-images.githubusercontent.com/60336145/139179481-f04f8e8e-25d4-467a-b66a-46f9ecef1428.png)
# I selected python because my Flask application needs it to run but you can choose the language that is needed for your application.  The second option ask if you want to upload your code or you want a sample application choose the "Sample application" option since we'll get our application's code from github.  Click on create Environment.
![image](https://user-images.githubusercontent.com/60336145/139179731-5a827d81-3c9b-4bb9-911b-b23c33246110.png)
# After the creation process is done we can see the health status of the Elatic BeanStalk.  Everything is green and healthy now is time to set up our jenkins intance.
![dep4-fix-4](https://user-images.githubusercontent.com/60336145/138937791-3e4fb78e-e3c5-4c28-873f-93b3e0c2db2c.png)
![deploy4-ebs](https://user-images.githubusercontent.com/60336145/138937810-69b798b8-60b3-4baf-9d22-a6ccd67557f1.png)
# Create an EC2 instance that has jenkins
# There are two ways of installing jenkins into your EC2 instance:
# 1. while in the process of making your EC2 instance add the set of commands of jenkins installation in the user data field:
![image](https://user-images.githubusercontent.com/60336145/139182185-5f655c10-7c26-40e2-9d50-2b8651520f48.png)
# 2. Run each command in a terminal once inside of your EC2
## ______________________________ Commands ___________________________________
### #!/bin/bash
### sudo yum update -y
### sudo wget -O /etc/yum.repos.d/redhat/jenkins.repo \ https://pkg.jenkins.io/redhat-stable/jenkins.repo
### sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
### sudo yum upgrade
### sudo yum install jenkins java-1.8.0-openjdk-devel -y
### sudo systemctl daemon-reload
### sudo systemctl start jenkins
## ___________________________________________________________________________
## 3. get the Public IP of your Jenkins EC2 and change it from "https://(your-public-ip)" to "http://(your-public-ip):8080" in your search bar to access jenkins
![image](https://user-images.githubusercontent.com/60336145/139183722-003b920e-638b-4e58-8174-367c0816ebc5.png)
## 4. After accessing jenkins you need to put the admin password which can be found inside your EC2 instance in this path highlighted in red. use the following commands: 
### **cd /** to go to your home directory
### **cat /var/lib/jenkins/secrets/initialAdminPassword**
# if you do not have access to the file change its permissions using the command 
### **chmod 700 /var/lib/jenkins/secrets/initialAdminPassword** 
## and then 
### **cat/var/lib/jenkins/secrets/initialAdminPassword**
![image](https://user-images.githubusercontent.com/60336145/139184205-8c0668cf-5fd0-4b83-b786-4126b9160244.png)
## after you successfully log into jenkins you need to install two plugings AWSEB pligin and Cloud beens credential plugin
![image](https://user-images.githubusercontent.com/60336145/139185361-1f00581f-1f8a-4e0f-a0e8-a855440e063a.png)
## follow these steps to install the plugins:
![image](https://user-images.githubusercontent.com/60336145/139185485-1f871d47-05df-48eb-974b-152d78a51113.png)
![image](https://user-images.githubusercontent.com/60336145/139185930-0c3daecc-5fa2-4c0c-8427-9f82d14bbcb4.png)
![image](https://user-images.githubusercontent.com/60336145/139186017-162978cd-bb01-41ec-a60d-396256e8491a.png)
## Once the plugins are installed we can start our project
![image](https://user-images.githubusercontent.com/60336145/139186184-5499910a-5164-49b2-8148-4899b338509e.png)
![image](https://user-images.githubusercontent.com/60336145/139186224-e456407f-8a5e-4948-aee4-e109f16a5507.png)
## In this part we will add our github repository link and create a credentials with a github personal token and our AWS user key pair
## [Click here to learn how to create a github personal token, this allows jenkins to coonect to our Github repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
## [Click here to learn how to make an AWS IAM user **Important: (This user needs to have Elastic BeasStalk administrator priviledges)** this gives jenkins access to our AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
![image](https://user-images.githubusercontent.com/60336145/139186844-4f3d19a2-7329-401c-8e62-21d58a2a4011.png)
![image](https://user-images.githubusercontent.com/60336145/139186985-2577cdd6-0101-4961-95ba-25f9122a66f8.png)
## Remember the Application name and the Environment name of our Elastic BeanStalk enter then here to tell jenkins which environment we want to use 
![image](https://user-images.githubusercontent.com/60336145/139187481-72879803-fed5-4c94-a83a-73c58e0ef63d.png)
## Next Enter a period "." in the Root field telling jenkins to use the all the files in our directory
![image](https://user-images.githubusercontent.com/60336145/139187799-078d437b-192b-46b5-8713-18300fc3a9df.png)
## Finally we need a version for our builds you can use "some text ${BUILD_ID}" to assign a progressing number as the version label
![image](https://user-images.githubusercontent.com/60336145/139187973-98fe7ae0-2ad9-4598-8c2a-41108629166c.png)
# Important if you are Deploying a Flask appication make sure the name of your main file is "**application.py**". AWS's elastic beanstalk will look for a file with this name to launch your application.
![image](https://user-images.githubusercontent.com/60336145/139189805-f9eed3bd-e9b1-414b-aa3a-e26a7245300d.png)
# Trouble along the way
## I found my deployements failing because the name of main file was not application.py after I changed that it worked smoothly.
## I also found that when building the version on the applicatoin is "sample application" then it runs health checks while deploying the new version this makes our environment unhealthy and the application cant deploy as a result.  I found that instead of deleting the whole environment and remaking it you can just restart the App's Web server and it will turn healthy after that jenkins will do a health check 30 times make sure you environment is healthy and the versions match then your deployment will be successful. 
![dep4-building-app-jenkins](https://user-images.githubusercontent.com/60336145/138937764-12ae389b-c141-47e0-9135-be3b024ebbe3.png)
![dep4-fix-2](https://user-images.githubusercontent.com/60336145/138937778-c314ea5d-cf95-4a96-9d81-bd2fc92b3da7.png)
![dep4-fix-3](https://user-images.githubusercontent.com/60336145/138937784-bfd7d941-6205-426a-a975-5e264db4152c.png)
![dep4-success](https://user-images.githubusercontent.com/60336145/138937817-d1c27c8b-1786-4cdb-98e2-eb5f2743d5d9.png)
![image](https://user-images.githubusercontent.com/60336145/139189704-2018e1fc-b351-4671-a98d-f50a6e1ebd57.png)

