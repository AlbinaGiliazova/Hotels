from django.contrib.auth.models import AbstractUser
from django.db import models

from food.constants import NULLABLE
from food.models import MealType


class CustomUser(AbstractUser):
    """Модель пользователя."""

    meal_type = models.ForeignKey(
        MealType,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="users",
        verbose_name="Тип питания",
    )
