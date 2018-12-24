# Product-Hunter-Django

## Downlaod Product-Hunter

You can get this project pretty easily. 

1. Just open a new Folder. 

2. Open up a git-bash and enter the following command:
    > git init

3. After init your git repositiory enter the following Command:
    > git clone https://github.com/DerAlexx/Product-Hunter.git

Now you got the project on your computer.

## Install Product-Hunter 

There are many things you have to install in order to run this project correctly.

### Requirementslist:
    1. Postgressql, MySQL, 
    2. Access to the SQL-Server
    3. ...

**We just tested this project with Prostgres so i would recommend you to use Postgres** 

### Reminder - Python and Django, etc.

You don't need to install Python or Django in any way. This projects will not only supply the sourcecode of 
the Webappliaction but also a buildin Pythoninterpreter aswell as all requiered dependences. 

**This project is working with Python 3.6.3 and Django 2.14 (more info about the Version used see the Freezepart below)**

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

**More Info at: https://docs.python.org/3/tutorial/venv.html**

### Databaseconnection

**It is importent to create a Database in your Databasemanagementsystems like Postgres, MySQL, ...**

Go to the **Settings.py** in *../src/product_hunter/product_hunter/settings.py*

Scroll Down to the section: **DATABASES**.

**Looks like:**

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql', --> Depending on the Databasesystem
            'NAME': 'yourDatabaseName', --> Name of the Database you created
            'USER':'yourDBusername',
            'PASSWORD': 'yourPassword', 
            'HOST':'localhost', --> This should be fine
            'PORT':'5432' --> This is the standard postgresport
        }
    }
    ```

**Enter all your information. Depending on your Databaseserversettings**

**Notice: All information in this section is just placeholder information! You need to add yours in order to run this Project** 

#### List of included Databasemanagementsystems
    1. SQLite
    2. PostgresSQL
    3. Oracle
    4. Redshift
    5. MS SQL Server 
    6. MySQL

### Run the Server

After connecting to the Database, navigate to *../src/product_hunter/* and run the following command:

> python manage.py migrate

In case this works fine your Database is working. In case this is not working, please check your entered information!

Finally run:

> python manage.py runserver

### Reach the Server

You can reach this server by entering in your Browser:

> http://localhost:8000/

Diffining your own port (As an example is choose 6666):

> python manage.py runserver 6666

You can reach this server by entering in your Browser:

> http://localhost:6666/

## Freezepart

### Python and Django

> Pythonversion 3.6.2

> Django 2.14

### Dependences:

    1. cx-Oracle==7.0.0
    2. db.py==0.5.3
    3. Django==2.1.4
    4. django-background-tasks==1.2.0
    5. django-compat==1.0.15
    6. django-filter==2.0.0
    7. django-rest-framework==0.1.0
    8. djangorestframework==3.9.0
    9. Markdown==3.0.1
    10. numpy==1.15.4
    11. pandas==0.23.4
    12. Pillow==5.3.0
    13. prettytable==0.7.2
    14. psycopg2==2.7.6.1
    15. pybars3==0.9.6
    16. PyMeta3==0.5.1
    17. python-dateutil==2.7.5
    18. pytz==2018.7
    19. six==1.12.0

## Thanks you and have a nice day!