# UW Side Project Club Website wooooooo

**Mac Setup:**
create a folder
for example:  /Users/Echo/Documents/MYFOLDER

clone the directory to a folder on your Mac
$ git clone https://github.com/keriwarr/SPC-website.git

$ cd SPC-website/

$ pip install virtualenv

use “pwd” and “cd” to make sure you are in /Users/Echo/Documents/MYFOLDER

$ python3 -m virtualenv SPC-website/

$ source SPC-website/bin/activate

After typing the line above, a line like this should show up: 
(SPC-website) v1020-wn-56-130:spc website Echo$ 

$ pip install Django

use “cd” and “pwd” to move to /Users/Echo/Documents/MYFOLDER/SPC-website/mysite

$ python3 manage.py migrate

$ python3 manage.py runserver

Then open your browser and go to “http://localhost:8000/spc_main/”
If everything works well, then you can see our SPC logo in the middle :)

***************************************************************************************

**Linux Setup:**

Install virtualenv for Python - pip install virtualenv

Create Python virtual environment spc-website in SPC-website directory - virtualenv spc-website

Install Django in virtualenv with pip - pip install Django

Run migrations before running servers for the first time

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

2. python/python3 manage.py makemigrations [name of app] - Creates DB migrations

3. python/python3 manage.py migrate - Runs DB migrations

**Admin stuff:**

python3 manage.py createsuperuser - Creates admin user

**File Structure:**

HTML files go in /mysite/spc_main/templates/spc_main

CSS files go in /mysite/spc_main/static/spc_main/stylesheets

JS files go in /mysite/spc_main/static/spc_main/scripts

All other assets go in /mysite/spc_main/static/spc_main/assets
