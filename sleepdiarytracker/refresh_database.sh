find . -path "/sleepdiarytracker/thesleeptrackerapp/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/sleepdiarytracker/thesleeptrackerapp/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations thesleeptrackerapp; #creates the migration.
python manage.py migrate; #runs the migration.  This will delete all of the data in your database.
#python manage.py loaddata user.json category.json product.json order.json payment_type.json  #loads the data from each .json file in sequential order.
