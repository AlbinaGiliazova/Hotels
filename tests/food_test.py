"""Тесты приложения."""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from food.models import MealType


@pytest.mark.django_db
def test_get_meal_price_success():
    # Создаём тестовый тип питания
    MealType.objects.create(type="breakfast", price=500.00)
    client = APIClient()
    url = reverse("meal_type/get_price")  # Имя формируется как basename-action

    response = client.post(url, {"type": "breakfast"}, format="json")

    assert response.status_code == 200
    assert response.json()["type"] == "Завтрак"
    assert float(response.json()["price"]) == 500.00


@pytest.mark.django_db
def test_get_meal_price_not_found():
    client = APIClient()
    url = reverse("meal_type/get_price")

    response = client.post(url, {"type": "nonexistent"}, format="json")
    assert response.status_code == 404
    assert "error" in response.json()
    assert response.json()["error"] == "Данный тип питания не найден."


@pytest.mark.django_db
def test_get_meal_price_no_type():
    client = APIClient()
    url = reverse("meal_type/get_price")

    response = client.post(url, {}, format="json")
    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"] == "Не указан тип питания."
