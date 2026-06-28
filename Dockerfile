FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/source

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=app.conf.development.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]