# What is this
This is a simple test of importing a csv with django command and reconciliate matching records and an APIView to retrieve this info

# How to install
We need a virtualenv with python 3.6 and a postgres database with a powered user (where you want, local, docker, rds..)

1. In virtualenv Install requirements
```
pip install -r requirements.txt
```
2. Copy env vars file
```
cp .env.example .env
```
2. Edit env vars with correct values (db and debug)

# How to import data
With a django command (--file is optional, by default is already getting data_samples/works_metadata.csv)
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
- Goto '/' path to open API Root
- In this view click on the first link that appears, /work/
- We see an error, it suggests us to use a GET query param to retrieve our work. Let's put "Shape of You" ISWC:
```
/work/?iswc=T9204649558
```
- tada! we have all out work information :)
