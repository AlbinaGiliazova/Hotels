"""Модель типов питания."""

from django.db import models

from meals.constants import (
    PRICE_MAX_DIGITS,
    TYPE_MAX_LENGTH,
)


class MealType(models.Model):
    """Модель типов питания."""

    MEAL_CHOICES = [
        ("No meal", "Без питания"),
        ("breakfast", "Завтрак"),
        ("breakfast_dinner", "Завтрак и ужин"),
        ("full", "Полный пансион"),
        ("all", "All inclusive"),
        ("ultra", "Ultra All inclusive"),
    ]
    type = models.CharField(max_length=TYPE_MAX_LENGTH, choices=MEAL_CHOICES)
    price = models.DecimalField(max_digits=PRICE_MAX_DIGITS, decimal_places=2)

    class Meta:
        verbose_name = "Тип питания"
        verbose_name_plural = "Типы питания"
        ordering = ["id"]

    def __str__(self):
        return f"{self.get_type_display()} — {self.price}₽"
