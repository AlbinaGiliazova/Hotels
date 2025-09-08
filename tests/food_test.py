"""Тесты приложения."""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from meals.models import MealType


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def meal_type():
    return MealType.objects.create(type="breakfast", price=100)


@pytest.mark.django_db
def test_list_meal_types(api_client, meal_type):
    url = reverse("mealtype-list")  # Убедись, что твой router назвал эндпоинт именно так
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data[0]["type"] == meal_type.type
    assert response.data[0]["price"] == meal_type.price


@pytest.mark.django_db
def test_retrieve_meal_type(api_client, meal_type):
    url = reverse("mealtype-detail", args=[meal_type.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["type"] == meal_type.type
    assert response.data["price"] == meal_type.price


@pytest.mark.django_db
def test_create_meal_type(api_client):
    url = reverse("mealtype-list")
    data = {"type": "full", "price": 200}
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert MealType.objects.filter(type="full", price=200).exists()


@pytest.mark.django_db
def test_update_meal_type(api_client, meal_type):
    url = reverse("mealtype-detail", args=[meal_type.id])
    data = {"type": "ultra", "price": 150}
    response = api_client.put(url, data)
    assert response.status_code == 200
    meal_type.refresh_from_db()
    assert meal_type.type == "ultra"
    assert meal_type.price == 150


@pytest.mark.django_db
def test_delete_meal_type(api_client, meal_type):
    url = reverse("mealtype-detail", args=[meal_type.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not MealType.objects.filter(id=meal_type.id).exists()
