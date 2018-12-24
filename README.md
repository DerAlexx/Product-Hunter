# Product-Hunter-Django

## Downlaod Product-Hunter

You can get this project pretty easyly. 

1. Just open a new Folder. 

2. Open up a git Bash with the following command:
    > git init

3. Enter the following Command:
    > git clone https://github.com/DerAlexx/Product-Hunter.git

## Install Product-Hunter 

There are many things you have to install in order to work with this project correctly.

### Requirementslist:
    1. Postgressql or an equivalent (We just tested this project with Prostgres so i would recommend you Postgres)
    2. Access to the SQL-Server
    3. ...

### Reminder - Python and Django, etc.

You dont need to install Python or Django in any way. This projects will not only supply the sourcecode of 
the Webappliaction but also buildin Python-Interpreter and all Dependences requiered to run this project. 

** This project is working with Python 3.6.3 and Django 2.14 (more info about the Version used see the Freezepart below) **

### Run this project

Navigate to the basicdirectory. 

#### Windows CMD:

> product-hunter\Scripts\activate.bat

#### Windows PowerShell:

> product-hunter\Scripts\activate.ps1

#### Linux and MacOS:

> product-hunter/bin/activate

#### Linux and MacOS with fish or csh:

> product-hunter/bin/activate.fish

or

> product-hunter/bin/activate.csh

You should now see on the left site the name of the project --> product-hunter

** More Info at: link:https://docs.python.org/3/tutorial/venv.html[runVenv] **

### Databaseconnection

Go to the ** Settings.py ** in * ../src/product_hunter/product_hunter/settings.py

Scroll Down to the section: ** DATABASES **.

Enter all your information. 

** Notice: All information in this section is just placeholder information! You need to add yours in order to run this Project ** 

After connecting to the Database, navigate to * ../src/product_hunter/ * and run the following command:

> python manage.py migrate

In case this works fine your Database is working. In case this is not working, please check your entered information!

Finally run:

> python manage.py runserver

You can reach this server by entering in your Browser:

> http://localhost:8000/

Diffining your own port (As an example is choose 6666):

> python manage.py runserver 6666

You can reach this server by entering in your Browser:

> http://localhost:6666/


## Thanks you 