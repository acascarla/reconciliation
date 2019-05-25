# What is this
This is a simple test of importing a csv with django command and reconciliate matching records and an APIView to retrieve this info

# How to install
You can start it with docker (with make aliases) or manually, in any case you will need an environment vars file, so first:
1. Copy env vars file
```
cp .env.example .env
```
2. Edit env vars with correct values (db and debug)

## Option 1. Docker
You need docker and docker-compose, then:
1. Build images and start services:
```
make run
```
2. Once django is running, apply migrations and create superuser
```
make init
```

## Option 2. Manual
If you prefer in raw, you need a virtualenv with python 3.6 and a postgres database with a powered user (where you want, local, docker, rds..)

1. In virtualenv install requirements
```
pip install -e .
```
2. Apply migrations
```
python manage.py migrate
```
3. Create superuser (if you need admin panel)
```
python manage.py createsuperuser
```
4. Start server
```
python manage.py runserver
```

# How to import data
With a django command
## Option 1: Docker
```
make import
```

## Option 2: Manual
Param --file is optional, by default is already getting data_samples/works_metadata.csv
```
python manage.py import_works_metadata --file data_samples/works_metadata.csv
```

# How to use API
Info:
We can use API Root client powered by REST Framework to make our lifes easier.
This project by now is not using any template view so we have the API Root client in the very begining of this app, in '/'.
Also, as Views we used a simple APIView instead of a ViewSet, ListAPIView or RetrieveAPIView.
By default APIView is not supported in API Root with DefaultRouter but we have a homemade "HybridRouter" that can handle API ViewSets and API Views, with this we can still use API Root.

How to:
1. Goto '/' path to open API Root
http://0.0.0.0:8000/
2. In this view we have to click on the first entry that appears
http://0.0.0.0:8000/work/
3. Now as response we see an error, that's GOOD becouse we have not given an ISWC and the error informs about that. Let's put "Shape of You" ISWC:
http://0.0.0.0:8000/work/?iswc=T9204649558
4. Tada! We see all info about this work :)
