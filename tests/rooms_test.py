import io

import pytest
from django.urls import reverse
from PIL import Image
from rest_framework.test import APIClient

from meals.models import MealType
from rooms.models import Room


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def meal_type(db):
    return MealType.objects.create(type="Завтрак", price=100)


def get_image_file():
    file = io.BytesIO()
    image = Image.new("RGB", (100, 100))
    image.save(file, "jpeg")
    file.name = "test.jpg"
    file.seek(0)
    return file


@pytest.mark.django_db
def test_create_room_with_nested(api_client, meal_type):
    url = reverse("room-list")  # Убедись, что basename роутера 'room'

    image_file = get_image_file()

    data = {
        "room_type": "suite",
        "meal_type": meal_type.id,
        "adults": 2,
        "children": 1,
        "area": 40,
        "quantity": 1,
        "double_bed": 1,
        "single_bed": 0,
        "amenities": [{"amenity_type": "general", "name": "Wi-Fi"}, {"amenity_type": "coffee", "name": "Кофе-машина"}],
        "rules": [{"name": "Курение", "rule_choice": "no"}],
        "photos": [{"image": image_file, "description": "Общий вид"}],
    }

    # Важно: для отправки файлов используем multipart
    resp = api_client.post(url, data, format="multipart")

    assert resp.status_code == 201
    room = Room.objects.get(id=resp.data["id"])
    assert room.amenity_set.count() == 2
    assert room.rules.count() == 1
    assert room.photos.count() == 1

    first_photo = room.photos.first()
    assert first_photo.description == "Общий вид"
    assert bool(first_photo.image)  # Фото должно быть сохранено
