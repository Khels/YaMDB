# YaMDb
### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
### Технологии
- Python 3.8.5
- Django 3.0.5
- Django Rest Framework 3.11.0
- gunicorn 20.0.4
- Docker 20.10.6
- docker-compose 1.25.0
- Nginx 1.19.3
- Postgres 12.4
### Начало работы

Пособие по установке Docker: https://docs.docker.com/engine/install/

И docker-compose: https://docs.docker.com/compose/install/

В .env файле размечена структура для понимания того, какими переменными окружения нужно его заполнять.

Для развёртывания приложения на основе контейнеров Docker нужно перейти в корневую директорию проекта и оттуда выполнить следующую команду:
```docker-compose up -d --build```

Чтобы остановить контейнеры достаточно:
```docker-compose stop```

А для их полного удаления (с удалением томов):
```docker-compose down -v```

Для создания суперпользователя сначала нужно выполнить миграции:
```docker-compose exec web python3 manage.py makemigrations api```
```docker-compose exec web python3 manage.py migrate --no-input```

И лишь после этого:
```docker-compose exec web python3 manage.py createsuperuser```

Для создания бэкап-файла БД нужно выполнить:
```docker-compose exec web python3 manage.py dumpdata > [YOUR_DUMP_FILE_NAME].json```

Для заполнения БД тестовыми данными:
```docker-compose exec web python3 manage.py loaddata fixtures.json```

##### Документация по API доступна по пути http://127.0.0.1/redoc/
### Автор
Khels Kelly
