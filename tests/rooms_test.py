import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..rooms.models import Bed, Room

User = get_user_model()


@pytest.fixture
def admin_user(db):
    user = User.objects.create_superuser(username="admin", password="password")
    return user


@pytest.fixture
def admin_client(admin_user):
    client = APIClient()
    client.login(username="admin", password="password")
    return client


@pytest.fixture
def bed(db):
    return Bed.objects.create(
        has_single=True,
        single_quantity=2,
        has_double=True,
        double_quantity=1,
    )


@pytest.fixture
def room(db, bed):
    return Room.objects.create(
        room_type="standard",
        meal_type=None,
        adults=2,
        children=0,
        area=25,
        quantity=1,
        beds=bed,
    )


def test_room_list(admin_client, room):
    url = reverse("room-list")  # Имя роутера, обычно app_label-room-list
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 1


def test_room_create(admin_client, bed):
    url = reverse("room-list")
    data = {
        "room_type": "standard",
        "meal_type": None,
        "adults": 2,
        "children": 1,
        "area": 30,
        "quantity": 1,
        "beds": bed.id,
    }
    response = admin_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Room.objects.filter(id=response.data["id"]).exists()


def test_room_retrieve(admin_client, room):
    url = reverse("room-detail", args=[room.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == room.id


def test_room_update(admin_client, room, bed):
    url = reverse("room-detail", args=[room.id])
    data = {
        "room_type": "deluxe",
        "meal_type": None,
        "adults": 3,
        "children": 1,
        "area": 40,
        "quantity": 1,
        "beds": bed.id,
    }
    response = admin_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    room.refresh_from_db()
    assert room.room_type == "deluxe"


def test_room_delete(admin_client, room):
    url = reverse("room-detail", args=[room.id])
    response = admin_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Room.objects.filter(id=room.id).exists()
