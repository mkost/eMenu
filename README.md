# eMenu
Project serving as online restaurant menu card

### Prepare database ###

* See instruction here: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04 or run steps below:
* sudo apt-get update
* sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
* sudo su - postgres
* psql
* CREATE DATABASE emenu;
* CREATE USER emenuuser WITH PASSWORD 'mypassword';
* ALTER ROLE emenuuser SET client_encoding TO 'utf8';
* ALTER ROLE emenuuser SET default_transaction_isolation TO 'read committed';
* ALTER ROLE emenuuser SET timezone TO 'UTC';
* GRANT ALL PRIVILEGES ON DATABASE emenu TO emenuuser;
* ALTER USER emenuuser CREATEDB;
* \q
* exit

### First installation ###

* Create virtualenv
* For correct working of uploading images do: sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
* create and activate virtualenv
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* enjoy reviewing the project :)
* static version - http://localhost:8000/default/
* asynchronous version - http://localhost:8000/
