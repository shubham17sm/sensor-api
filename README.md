# sensor-api
HC-SR04 with NodeMCU (ESP 8266) realtime API using Django REST API



# Getting Started

First Create and start your virtual environment:
```
  Clone or download this repository
  virtualenv -p python3 .
  pip install -r requirement.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
```

# Post Installation
Go to the web browser and visit http://127.0.0.1:8000/

Admin username: admin

Admin password: admin

To Make API calls using [POSTMAN](https://www.postman.com/). Create new user and create a token for user and send request through POSTMAN.

