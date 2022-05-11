FROM python:3.8-slim-buster

#ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
VOLUME ./db.sqlite3 /app
COPY . .
#CMD ["python","manage.py","makemigrations"]
#CMD ["python","manage.py","migrate"]
#CMD ["python","manage.py","migrate"]
#docker exec web ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('your_user', 'your_password')"

CMD ["python","manage.py","runserver","0.0.0.0:8002"]