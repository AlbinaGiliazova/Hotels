import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from hotels.models import Hotel, VacationType


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def vacation_type(db):
    return VacationType.objects.create(name="Семейный")


@pytest.mark.django_db
def test_create_hotel_with_nested(api_client, vacation_type):
    url = reverse("hotels-list")  # Зависит от basename в DefaultRouter (например, 'hotel')

    data = {
        "name": "Отель Тестовый",
        "vacation_type": vacation_type.id,
        "hotel_type": "hotel",
        "category": 4,
        "country": "Россия",
        "city": "Калуга",
        "address": "ул. Победы, 15",
        "latitude": 55.44,
        "longitude": 37.777,
        "check_in_time": "14:00:00",
        "check_out_time": "12:00:00",
        "description": "Пример отеля для теста.",
        "amenities": [{"amenity_type": "general", "name": "Wi-Fi"}, {"amenity_type": "room", "name": "Кондиционер"}],
        "rules": [
            {"name": "Курение запрещено", "is_checked": True, "description": "Во всех помещениях"},
            {"name": "Можно с животными", "is_checked": False, "description": "Только мелкие животные"},
        ],
        "distances": [{"name": "ЖД вокзал", "value": 3000}, {"name": "Центр города", "value": 1200}],
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == 201

    hotel = Hotel.objects.get(id=response.data["id"])
    assert hotel.amenities.count() == 2
    assert hotel.rules.count() == 2
    assert hotel.distances.count() == 2
    assert hotel.name == data["name"]
    assert hotel.description == data["description"]
