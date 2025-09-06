# Hotels
Сайт про отели

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
