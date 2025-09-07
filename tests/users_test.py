import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestUserViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.url = reverse("user-list")
        self.password = "Test1234"
        # Создаём пользователя для списка и получения
        self.user = User.objects.create_user(email="test@example.com", password=self.password)

    def test_list_users(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert any(u["email"] == self.user.email for u in response.data)

    def test_retrieve_user(self):
        url_detail = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url_detail)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == self.user.email

    def test_create_user(self):
        data = {"email": "newuser@example.com", "password": "NewPass123"}
        response = self.client.post(self.url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email="newuser@example.com").exists()

    def test_create_user_invalid(self):
        data = {"email": "", "password": ""}
        response = self.client.post(self.url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_method_not_allowed_put(self):
        url_detail = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url_detail, {"email": "changed@example.com"})
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_method_not_allowed_delete(self):
        url_detail = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url_detail)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_set_meal_type(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("user-set-meal-type")
        data = {"meal_type": "breakfast"}  # Подберите правильное название и допустимое значение
        response = self.client.post(url, data, format="json")
        assert response.status_code == 200
        assert response.data["message"] == "Тип питания обновлён"
        self.user.refresh_from_db()
        assert self.user.meal_type == "breakfast"
