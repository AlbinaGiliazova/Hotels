from django.contrib.auth.models import AbstractUser
from django.db import models

from hotels.models import Hotel
from meals.constants import NULLABLE
from meals.models import MealType
from rooms.models import Room


class CustomUser(AbstractUser):
    """Модель пользователя."""

    meal_type = models.ForeignKey(
        MealType,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="users",
        verbose_name="Тип питания",
    )
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="users",
        verbose_name="Отель",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="users",
        verbose_name="Номер",
    )
