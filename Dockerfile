FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app

RUN ["chmod", "+x", "/app/entrypoint.sh"]
RUN pip install -r req.txt

EXPOSE 8000
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
