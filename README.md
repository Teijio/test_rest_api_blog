[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)


#
Тестовое задание django rest api

## Подготовка сервера

```bash
# Создайте файл .env в директории проекта и укажите в нем:
SECRET_KEY #'< секретный ключ >'
POSTGRES_USER #postgres
POSTGRES_PASSWORD #postgres
POSTGRES_DB  #postgres
DB_NAME #blog
DB_HOST #db
DB_PORT #5432

```

Все действия мы будем выполнять в Docker, docker-compose.

## Запуск

Запустите контейнер командой docker-compose up

Выполните по очереди команды:

```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```

При необходимости, загрузите тестовые данные.
В файле scripts.py можете указать необходимое количество.

```bash
docker-compose exec backend python scripts.py
```

Теперь проект доступен по адресу http://localhost:8000/api/.

###
Автор проекта - Артур Шутов
###
