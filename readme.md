# Django quiz application

## Installation
- Clone the repo
```
git clone git@github.com:shankarlmc/csitan-django-workshop.git
```
- Change the dir and setup requirements
```
cd csitan-django-workshop
python3 -m venv .venv
source .venv/bin/activate # for linux or mac
.venv\Scripts\activate # for windwos
pip install -r requirements.txt
```
- Setup .env file
```
cp .env-sample .env
```
- Migrate and run application
```
python3 manage.py migrate
python manage.py runserver
```