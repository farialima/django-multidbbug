
# Project created with:

```
poetry install
poetry run django-admin startproject multidbbugsite
poetry run django-admin startapp multidbbugapp
mv multidbbugapp tmp
mv tmp/* .
rmdir tmp
```

# To set up things

```
rm -f *.sqlite3
poetry run ./manage.py migrate --database default
poetry run ./manage.py migrate --database other
poetry run ./manage.py createsuperuser --username admin --email admin@test.com
poetry run ./manage.py runserver
```

# To reproduce the problem

 - go to http://localhost:8000
 - login
 - go to http://127.0.0.1:8000/admin/multidbbugapp/parcel/1/change/
 - edit value to "two" (which correspond to an object in the default database, see migration file)
 - see error