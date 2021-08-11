# Django-User_Accounts
This project is based on `Django` a Python-based free and open-source web framework that follows the model-view-controller architectural pattern, dealing with user accounts and register/login & password-reset functionalities.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://myusersapp.herokuapp.com)

## How to run on local server?
The project requires Python 3.6 or 3.7 (The version of Django is specified in requirements.txt).
I suggest creating a new virtual environment:
### You can create and activate your vitual environment using conda or pip
in-case you dont know how to create a virtual environment, follow the below steps:
>>> using conda
```
conda create --name My_Env_Name
conda activate My_Env_Name
```
>>> using python
```
python -m venv My_Env_Name
source My_Env_Name/bin/activate
```

Activate your virtual environment, then running:
```
gitclone https://github.com/Sanju525/Django-User_Accounts.git
cd Django-User_Accounts
pip install -r requirements.txt
```

will download the project and install all the packages for running the application.
### Changes in the project
To run this project in your local machine, we need to do certain changes to our project.
#### settings.py
In the proect folder **Django-User_Accounts** goto UserAccounts and open `settings.py` file in any editor. The first thing you need to change is the `SECRET_KEY` you can replace that with any randomtext or you can generate and copy a random string from python inbuilt package `secrets`, simply open python-interpreter and import package by `import secrets` and execute as follows,
```
>>> import secrets
>>> secrets.token_hex(24)
```
copy the string and replace it in the SECRET_KEY variable. After that change the `DEBUG` value to `True` and remove 'myusersapp.herokuapp.com', from ALLOWED_HOSTS set.

#### Working with password reset in the project
You need to change few more values in the `settings.py` file for resetting the user passwords. Open the `settings.py` file and you will see variables `EMAIL_HOST_USER` and `EMAIL_HOST_PASS`, change those values with your email and **Google app passwords** respectively.

#### Creating tables and super-user for storing data and administrating the application
>>> Creating tables

To create tables you simply, change the directory to Django-User_Accounts {the directory containing `manage.py` file.}
open up commandline or terminal and type the following command to create tables.
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

>>> Creating superuser for app administration.
```
python manage.py createsuperuser
```

after executing the above command you will be requested to provide username, email and password, fill those and you are now good to go.

### Run the application
In commandprompt/terminal `cd` to Django-User_Accounts directory, execute the following command
```
python manage.py runserver
```
Open the browser and goto `127.0.0.1:8000`.

### for site administration 
goto `127.0.0.1:8000/admin` fill the username and password used for creating superuser, then you will be redirected to `Django-admin` page.


