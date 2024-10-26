#!/usr/bin/env bash

# Переменные для подключения к базе данных
host="db"
port="5432"

# Ожидание доступности сервера PostgreSQL
echo "Проверка доступности базы данных PostgreSQL..."

# Используем nc для ожидания открытия порта PostgreSQL
until nc -z "$host" "$port"; do
  echo "Postgres недоступен - ожидание..."
  sleep 1
done

echo "Postgres доступен - выполняем команды Django"

# Остановка выполнения скрипта при ошибке
set -e

# Выполняем миграции и запускаем сервер
python manage.py migrate

python manage.py runserver 0.0.0.0:8000


