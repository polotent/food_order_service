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
Create "delivery_food" database in PostreSQL. Create "django" user with "django" password and provide rights to operate with database.

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

### Protocol description
There are 4 basic functions supported:
1. Get list with all available restaurants (restaurants)
1. Get list with menu name and menu items for specified restaurant (menu)
1. Set items to order and quantity for each item (preorder)
1. Finilize order, specifying user address and user phone number (order).

Each function has its own URL to make request to. All request are POST. All request data format, if present, is JSON. All responses data format is JSON.

If error occurs during request processing, the response is return with error message. Example error response:
```
{
    "error": "Error message text"
}
```

#### Restaurants
URL:
```
/orders/restaurants
```

Response example:
```
{
    "restaurants": [
        {
            "restaurant_name": "Georgian Heaven",
            "menu_id": 1
        },
        {
            "restaurant_name": "Tasty Burgers",
            "menu_id": 2
        }
    ]
}
``` 

#### Menu
URL:
```
/orders/menu
```

Request example:
```
{
    "menu_id": 1
}
```

Response example:
```
{
    "menu_name": "Georgian cuisine",
    "menu_items": [
        {
            "id": 1,
            "item_name": "Shashlik",
            "item_price": 400
        },
        {
            "id": 2,
            "item_name": "Potatoes",
            "item_price": 300
        },
        {
            "id": 3,
            "item_name": "Georgian Salade",
            "item_price": 250
        }
    ]
}
```

#### Preorder
URL:
```
/orders/preoder
```

Request example:
```
{
    "items": [
        {
            "id": 1,
            "quantity": 2
        }
    ]
}
```

Response example:
```
{
    "order_id": 1,
    "total_price": 800,
    "status": "registered"
}
```

#### Order
URL:
```
/orders/order
```

Request example:
```
{
    "order_id": 1,
    "user_addr": "Kazan, Lenina str, 89",
    "user_phone": "+79608765678"
}
```

Response example:
```
{
    "status": "accepted"
}
```

### Tests
Run tests with:
```
python manage.py test
```
