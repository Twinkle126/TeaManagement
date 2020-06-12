# README #

Content management system for Sadguru' Amrit Tulya Tea Shop.
See app's screen shot with some products-
![Alt text](appPage.JPG?raw=true "APP Product Detail Page")

### What is this repository for? ###

thinkbridge repo code is a my solution to the assignment given by ThinkBridge,
Here admin can create users, provide access, create,edit and delete tea products related data in this panel.
This cms is build on Django, SQLite3 and Python

### How do I get set up? ###

This project has been created in following environment
1. Anaconda(Python 3.6.10 version)
Download link:https://www.anaconda.com/download/#linux
2. Django 3.0.7
Installation steps:pip install Django
3. SQLite3

### How to run ###
1. Navigate your terminal/anaconda cmd prompt to the directory where the project.
2. Run the following commands-
A. pip install -r requirements.txt -> This will install all dependencies
B. python manage.py makemigrations 
C. python manage.py migrate
D. python manage.py createsuperuser -> This will ask to create admin's username/password
E. python manage.py runserver -> This will start the server at your host
3. In your browser, go to "http://YOUR_HOST:PORT_NUM"( default PORT_NUM is 8000)
4. Login with admin/admin (default username and password)

### How to test in cloud ###
Code is deployed on Heroku and can be accessed with below link:
https://product-inventory-webapp.herokuapp.com/

Above link can be in ideal stage due to Heroku free tier usage but- 
can be activated by just restarting the server.

### How to test UnitTest ###
1. Navigate your terminal/anaconda cmd prompt to the directory where the project.
2. Run the following commands--
A. coverage run --source='.' manage.py test inventory
B. coverage report
C. coverage html
3. Go to the project root directory and open index.html file from htmlcov folder
See test coverage report screen shot here-
![Alt text](testCoverageReport.JPG?raw=true "Test Coverage Report")

### My Github Repo link ###
https://github.com/Twinkle126/TeaManagement

