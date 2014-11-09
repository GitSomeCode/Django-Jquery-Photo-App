@echo off

IF EXIST media\ (
@echo "Deleting '/media' directory..."
@echo.
rmdir /S /Q media
)

@echo "Deleting sqlite3 database..."
@echo.
del db.sqlite3

IF "%1"=="" (
@echo "Migrating the database..."
@echo.
python manage.py migrate
)