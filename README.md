# Hotels
Сайт про отели.

Реализовано:

- типы питания,
- создание и выбор отеля с различными удобствами,
- создание и выбор номера с различными удобствами,
- тесты.


# Как установить

Скачайте с помощью команды:

git clone https://github.com/AlbinaGiliazova/Hotels.git

cd Hotels

Установите Python 3.12 и Docker.

pip install poetry

Создайте папку test с пустым файлом __init__.py

poetry install

Переименуйте .env.sample в .env

python

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

exit()

Вставьте полученный ключ в .env

Также впишите свой емайл и пароль в .env

pip install pre-commit

pre-commit install

docker compose up -d --build

Сайт будет находиться по адресу в браузере 127.0.0.1:80.

Создать суперпользователя:

docker-compose exec app python manage.py createsuperuser

Админка находится по адресу 127.0.0.1/admin.

Swagger UI будет доступен по адресу: [`/api/docs/`](http://localhost:8000/api/docs/)

JSON-схема OpenAPI: [`/api/schema/`](http://localhost:8000/api/schema/)
