from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from meals.constants import NULLABLE
from meals.models import MealType
from rooms.constants import (
    AMENITY_TYPE_MAX_LENGTH,
    DOUBLE_BED_MAX_QUANTITY,
    NAME_MAX_LENGTH,
    ROOM_TYPE_MAX_LENGTH,
    RULE_CHOICE_MAX_LENGTH,
    SINGLE_BED_MAX_QUANTITY,
)


class Amenity(models.Model):
    """Удобства."""

    AMENITY_TYPE = [
        ("general", "Общие"),
        ("coffee", "Кофе-станция"),
        ("bathroom", "В ванной комнате"),
        ("view", "Вид"),
    ]
    amenity_type = models.CharField(
        "Тип удобств",
        max_length=AMENITY_TYPE_MAX_LENGTH,
        choices=AMENITY_TYPE,
        default="general",
    )
    name = models.CharField("Название", max_length=NAME_MAX_LENGTH)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Удобства номера"
        verbose_name_plural = "Удобства номера"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Rule(models.Model):
    """Правила номера."""

    RULE_CHOICES = [
        ("yes", "Разрешено"),
        ("no", "Запрещено"),
    ]
    room = models.ForeignKey("Room", related_name="rules", on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    rule_choice = models.CharField(
        "Правило",
        max_length=RULE_CHOICE_MAX_LENGTH,
        choices=RULE_CHOICES,
        default="no",
    )

    class Meta:
        verbose_name = "Правило номера"
        verbose_name_plural = "Правила номера"
        ordering = ["name"]

    def __str__(self):
        return self.name


class RoomPhoto(models.Model):
    """Фотографии номера."""

    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.HOTEL_PHOTOS_FOLDER)
    description = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)

    class Meta:
        verbose_name = "Фотография номера"
        verbose_name_plural = "Фотографии номера"
        ordering = ["room__id"]

    def __str__(self):
        return f"Фото {self.room.id}"


class Room(models.Model):
    """Номер."""

    ROOM_TYPES = [
        ("standard", "Standard"),
        ("single", "Single Room"),
        ("double", "Double Room"),
        ("twin", "Twin Room"),
        ("triple", "Triple Room"),
        ("family", "Family Room"),
        ("superior", "Superior Room"),
        ("deluxe", "Deluxe Room"),
        ("studio", "Studio"),
        ("suite", "Suite"),
        ("junior", "Junior Suite"),
        ("residence", "Residence"),
        ("royal", "Royal Suite"),
        ("penthouse", "Penthouse"),
    ]
    room_type = models.CharField(
        "Тип номера",
        max_length=ROOM_TYPE_MAX_LENGTH,
        choices=ROOM_TYPES,
        default="standard",
    )
    meal_type = models.ForeignKey(
        MealType,
        on_delete=models.SET_NULL,
        verbose_name="Тип питания",
        related_name="rooms",
        null=True,
    )
    adults = models.PositiveSmallIntegerField(
        "Количество проживающих взрослых",
        default=0,
    )
    children = models.PositiveSmallIntegerField(
        "Количество проживающих детей",
        default=0,
    )
    area = models.PositiveSmallIntegerField(
        "Площадь, м²",
        default=25,
    )
    quantity = models.PositiveSmallIntegerField(
        "Количество номеров этой категории",
        default=1,
    )
    double_bed = models.IntegerField(
        "Двуспальная кровать",
        help_text="Двуспальная кровать",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(DOUBLE_BED_MAX_QUANTITY),
        ],
        **NULLABLE,
    )
    single_bed = models.IntegerField(
        "Односпальная кровать",
        help_text="Односпальная кровать",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(SINGLE_BED_MAX_QUANTITY),
        ],
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        ordering = ["id"]

    def __str__(self):
        return f"Номер {self.id}"
