# UW Side Project Club Website wooooooo

**Setup:**

Create Python virtual environment in SPC-website directory

Install Django in virtualenv with pip

**Useful Terminal Commands (if python doesn't work try using python3):**

python/python3 - Run Python

python/python3 -m venv [name of virtual env] - Create a virtual environment

source [name of virtual env]/bin/activate - Activates virtual environment (spc-website)

pip install - Install frameworks/libraries

deactivate - Deactivates virtual environment

python/python3 manage.py startapp [name of app] - Creates a Django app

python/python3 manage.py runserver - Runs Django server

python/python3 manage.py shell - Starts Python shell

**Updating models:**

1. Edit in models.py

2. python3 manage.py makemigrations [name of app] - Creates DB migrations

3. python3 manage.py migrate - Runs DB migrations

**Admin stuff:**

python3 manage.py createsuperuser - Creates admin user
