# YaMDb
### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
### Начало работы

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