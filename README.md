# Food order service
## Description
REST server prototype for application for ordering food from restaurants. Made in Python 3 using Django 3.2 framework.

Currently there is only development prototype with hardcoded settings. In production all needed settings would be moved to environment variables.
## Requirements
* PostgreSQL
* Python 3
* pip for python 3
## Installation
### Pipenv
Install pipenv with:
```
pip install pipenv
```
### Project packages
cd to root directory of the project and install all needed packages with:
```
pipenv install
```
## Usage
### Configuration
Create 'delivery_food' database in PostreSQL. Create 'django' user with 'django' password and provide rights operate with database.

### Launching
Migrate with:
```
python manage.py migrate orders
```
To seed test data, use:
```
python manage.py seed
```
Run django server:
```
python manage.py runserver
```

All logs are saved to 

food_order_service\orders\logs\ordersapp.log

### Tests
Run tests with:
```
python manage.py test
```
