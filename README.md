# CarDj

Тестовое задание

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Описание проекта

Тестовоое задание. На урле '/' сразу открывается сваггер для удобства.

Докер добавлен для демонстрации возможности работы с ним.
Image на докерхаб не делал.

## Установка проекта локально

* Склонировать репозиторий на локальную машину:

```bash
git clone https://github.com/p17m0/CarDj
cd backend
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

* Cоздайте файл `.env` в директории `/backend/` с содержанием:

```
DB_ENGINE=
DB_NAME=
POSTGRES_USER=s
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
```

* Перейти в директoрию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pip install -r requirements.txt
```

* Выполните миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Запустите сервер:

```bash
python manage.py runserver
```
