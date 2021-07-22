release: python manage.py makemigrations app_2 --no-input
release: python manage.py makemigrations app_1 --no-input

release: python manage.py migrate --database=users_db --no-input
release: python manage.py migrate --database=company_db --no-input


web: gunicorn petrolapp.wsgi
