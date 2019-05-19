Simple test of importing a csv with django command and reconciliate matching records

1. Install requirements
```
pip install -r requirements.txt
```
2. Create postgres db
```
createdb {{ db_name }}
```
3. Set env vars
```
cp .env.example .env
```
4. Import data with command
```
python manage.py import_works_metadata --file data_samples/works_metadata.csv
```
