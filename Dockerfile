FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app

RUN pip install -r req.txt
EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
RUN python manage.py makemigrations wallet
CMD ["python", "manage.py", "runserver", '0.0.0.0:8000']