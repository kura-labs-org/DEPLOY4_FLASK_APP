# DEPLOY04_FLASK_APP

<h1 align=center>Custom Application - YouTube Converter</h1>


(This is for educational purposes)


As a person who listens to music a lot, I wanted to make this application to make my life a little easier. I prefer to work on projects that benefit me. For example, I made a VPN application so I can use it. I prefer to download music online and put it on my phone rather than using streaming services. I do not like paywalls so I thought this was a great project for me. It's a weird way of listening to music but I have been doing it for a long time since Limewire days.


While looking up ideas, I faced some issues.I tried looking up official YouTube APIs to download videos but I found out it's not supported because it's against their terms of services so I had to look for different options. I came across this repository and thought it would be great to add on. The repo creator supplies an API that I could use to embed into a website. It gives the user different options to download videos in different qualities. While creating the application, I used Ibrahima’s repository as a template. His repository was a great way to understand how to write to HTML files and use variables in them. Everything was simple and easy to understand. While creating the application, I found this really great way of getting the YouTube ID and thought it would be great to incorporate it.


For my application, once a user enters the URL inside the web page and presses convert, it would do a GET method. This would then call the converter() function inside of application.py and that would get the string the user entered. The application will then call a id_grabber function from the helper.py file, and that will use urlparse to parse the URL and extract the youtube ID from the URL. It goes to many different cases to incase the user enters a different youtube link format. Once it gets the ID it will return the ID in a variable called youtube_id. The youtube_id will then concat with a string to the API and be assigned to a variable called api_converter_link. This is then returned into a function called render_templates() which basically renders a template from the template folder which has an index.html file. This will basically let the HTML page use variables.

- URL Shortener Application: https://github.com/Deodutt/DEPLOY4_FLASK_APP
- To Do Application: https://github.com/Deodutt/HW-todo-api
- YouTube Converter Application: https://github.com/Deodutt/YouTube-to-MP3-Converter-API

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
