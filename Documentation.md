# Documentation

# Table of Contents
- AWS 
  Elastic Beanstalk 

-  Linux
-  Jenkins 

## Terminal
First SSH into the instance

```
sudo yum update -y

sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

sudo yum upgrade

sudo yum install jenkins java-1.8.0-openjdk-devel -y

sudo systemctl daemon-reload

sudo systemctl status jenkins

```
These specific commands were used because the dependencies neccessary needed to be downloaded but Jenkins was already installed on the instance. 

I inserted the public IP of the EC2 instance with attached to :8080

![Screen Shot 2021-12-14 at 11 09 17 AM](https://user-images.githubusercontent.com/84725239/146117174-0f4cdca2-fda3-4b58-92d5-5402683c43e7.png)

Add plugins required for completion of assignment

![Screen Shot 2021-12-14 at 10 26 01 AM](https://user-images.githubusercontent.com/84725239/146121111-434b9179-beb4-4f10-aa08-ef418bc4aeeb.png)

![Screen Shot 2021-12-14 at 10 26 23 AM](https://user-images.githubusercontent.com/84725239/146121140-c11cea28-2e8d-470c-b53b-c74c925d6498.png)

The two plugins were AWSEB Deployment Plugin and Cloudbees AWS Credentials Plugin.

![Screen Shot 2021-12-14 at 10 27 14 AM](https://user-images.githubusercontent.com/84725239/146121178-2f9df533-8ae2-4cfe-bbb1-4cf63f1b770a.png)

![Screen Shot 2021-12-14 at 10 27 28 AM](https://user-images.githubusercontent.com/84725239/146121211-881c6d8b-511f-4d5a-bf8e-97555ea6ac3b.png)


After, adding the plugins I created a multibranch pipeline.

![Screen Shot 2021-12-14 at 10 28 04 AM](https://user-images.githubusercontent.com/84725239/146123012-1bea216d-21b1-45c5-9fe9-97d3609c4533.png)



The GitHub repository was the repo from which I wanted to utilize for Multibranch pipeline. For my credentials I needed my AWS access and secret key. Found within the 


![Screen Shot 2021-12-14 at 10 38 33 AM](https://user-images.githubusercontent.com/84725239/146123075-58524450-ed25-4b9a-889e-1b1605614391.png)

The Access Key was needed here as well as the region that is used.

![Screen Shot 2021-12-14 at 10 39 17 AM](https://user-images.githubusercontent.com/84725239/146123098-70f9d30b-a2d2-4322-812c-d78f073859b7.png)

For the application name and environment portion I used the ones I named in AWS Elastic Beanstalk.

![Screen Shot 2021-12-14 at 10 40 51 AM](https://user-images.githubusercontent.com/84725239/146123107-4b1da70d-769e-4d25-acc5-e8dbb8138725.png)

Check the health of the environment to see if it everything functional.

![Screen Shot 2021-12-14 at 11 16 42 AM](https://user-images.githubusercontent.com/84725239/146123134-7d8ae81b-7402-43a1-93d0-3b6f1072b3ae.png)

After I deployed the application using the link located in the slide above in Elastic Beanstalk.

![Screen Shot 2021-12-14 at 11 15 04 AM](https://user-images.githubusercontent.com/84725239/146123172-ed4260c3-652e-46e6-87ae-2408016fcae0.png)

After the 4th build was completed the application was able to run.
The following screenshot is the url shortner page 

![Screen Shot 2021-12-14 at 11 17 55 AM](https://user-images.githubusercontent.com/84725239/146123218-b5105c8a-6309-4fa2-92e4-fc0972d49367.png)




