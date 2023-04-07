# Boilerplate For Django-Rest-Framework

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![python badge](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white)
![nginx badge](https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white)
![gunicorn badge](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white)
![mysql badge](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white)
![docker badge](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white)
![jwt badge](https://img.shields.io/badge/JSON_Web_Tokens-000000?style=flat-square&logo=JsonWebTokens&logoColor=white)

## Quick start on DRF project
* JWT authentication flow integrated
* email based username, email based identification
* essential drf related packages included (ex. djangorestframework-camel-case etc)
* basic user app created
* custom exception handler
* custom renderer
* setting.py separated for each dev and production environments
* some custom permission classes
* AWS S3 integration 
* swagger documentation via drf-yasg
* mypy, pytest configuration
* Dockerfile for DRF
* Docker Compose file for DB (mysql), Nginx, Django app
* Nginx basic configuration files (public.conf, upstream.conf, nginx.conf)
* Dockerfile for nginx container
* init.sql file for mysql container initialization
* and some more...

## Getting Started
```shell
git clone https://github.com/EarthlyZ9/DRF-Boilerplate.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 manage.py runserver
```