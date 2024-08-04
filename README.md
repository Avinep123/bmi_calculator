To run the project


To create database in MYSQL
create database bmi;
use bmi;
After creating database
Go to settings.py in bmi/settings.py and enter your user,password,host & portno here;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'bmi',
        'USER': 'root',
        'PASSWORD': '1579',
        'HOST': '127.0.0.1',   
        'PORT': '3306',
    }
}

now run 
python manage.py makemigrations
python manage.py migrate
and python manage.py runserver to run the project

