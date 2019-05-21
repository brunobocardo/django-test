# How is My Team?
A simple Django application to allow daily checkins and monitoring of your teams happiness.

## Application functionalities
* Permit users to login.
* Users can answer just once their happiness level per day.
* After answered the question or revisit this application, user will see a anonymously statistics page about his team. 
* When the admin user access the Application, they can see the anonymously statistics page of all teams and users.
* Admin user can add users and Teams using Django Admin page.

## Requirements

To run this simple Django application you will need:

1. Docker installed

## Install
1. Clone this project into your pc
2. Go to this directory ".../django-test/"
3. Run the command to build the image to our Docker ```sudo docker build -t django-test -f deploy/Dockerfile . ```
4. After, Run the command to run our container ```sudo docker run -d --name django-test-survey -p 9000:9000 --restart=always django-test```

## Default credentials
There is an admin account created to this application.

Credentials are:
* User: ``` admin ```
* Passwd: ``` @pacoca123 ```
* Email: ``` admin@d1g1t.com ```

## Instructions
To use this application, admin user needs to create new users and teams

To start use this application:
1. Go to http://localhost:9000/admin/
2. In the section ``` AUTHENTICATION AND AUTHORIZATION ```, click on Add an User and input username and password, after click on save.
3. After create an user, go to back to Django admin page, and go to section ``` DJANGO_SURVEY ```, click on Add a Group to create a Team, input the name and click on save.
4. Last step is add the user created into User profiles, go to back to Django admin page, click on Add User profiles, select an user and a group and click on save. ***The group is not required***
5. The users now can login and answer the question.

## Points to improve
* Create a series historical about the happiness of the team for the last 3 months.
* An user can select what Teams they want to monitor and see statics about them
