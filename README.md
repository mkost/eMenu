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
* \q
* exit

### First installation ###

* Create virtualenv
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* enjoy reviewing the project :)
