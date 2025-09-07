import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from hotels.models import Hotel, VacationType

User = get_user_model()


@pytest.fixture
def admin_user(db):
    user = User.objects.create_superuser(username="admin", password="admin123", email="admin@test.com")
    return user


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def vacation_type(db):
    return VacationType.objects.create(name="Активный отдых")


@pytest.mark.django_db
def test_admin_can_create_hotel(api_client, admin_user, vacation_type):
    api_client.force_authenticate(user=admin_user)
    data = {
        "name": "Test Hotel",
        "vacation_type": vacation_type.id,
        "hotel_type": "hotel",
        "category": 5,
        "country": "Россия",
        "city": "Москва",
        "address": "Ул. Тестовая, 1",
        "latitude": 55.7558,
        "longitude": 37.6176,
        "description": "Лучший отель Москвы",
        "check_in_time": "14:00",
        "check_out_time": "12:00",
    }
    url = reverse("hotel-list")
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert Hotel.objects.filter(name="Test Hotel").exists()


@pytest.mark.django_db
def test_admin_can_list_hotels(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse("hotel-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_non_admin_cannot_create_hotel(api_client):
    url = reverse("hotel-list")
    data = {
        "name": "Forbidden Hotel",
        "hotel_type": "hotel",
        "category": 3,
        "country": "Россия",
        "city": "Москва",
        "address": "Ул. Закрытая, 10",
        "latitude": 55.7558,
        "longitude": 37.6176,
        "description": "Должно быть запрещено",
        "check_in_time": "14:00",
        "check_out_time": "12:00",
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 403


@pytest.mark.django_db
def test_non_admin_cannot_list_hotels(api_client):
    url = reverse("hotel-list")
    response = api_client.get(url)
    assert response.status_code == 403
