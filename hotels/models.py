from datetime import time

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from food.constants import NULLABLE
from hotels.constants import (
    ADDRESS_MAX_LENGTH,
    CITY_MAX_LENGTH,
    DISTANCE_TYPE_MAX_LENGTH,
    HOTEL_MAX_LENGTH,
    HOTEL_TYPE_MAX_LENGTH,
    NAME_MAX_LENGTH,
    VACATION_TYPE_MAX_LENGTH,
)


class VacationType(models.Model):
    """Тип отдыха. Варианты значений задаются в админке."""

    name = models.CharField("Название типа отдыха", max_length=VACATION_TYPE_MAX_LENGTH, unique=True)

    class Meta:
        verbose_name = "Тип отдыха"
        verbose_name_plural = "Типы отдыха"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DistanceType(models.Model):
    """До какого объекта берется расстояние."""

    name = models.CharField("Тип объекта", max_length=DISTANCE_TYPE_MAX_LENGTH, unique=True)

    class Meta:
        verbose_name = "Тип объекта для расстояния"
        verbose_name_plural = "Типы объектов для расстояния"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Distance(models.Model):
    """Расстояние."""

    distance_type = models.ForeignKey(
        DistanceType, on_delete=models.CASCADE, verbose_name="Тип объекта", related_name="distances"
    )
    value = models.PositiveIntegerField(
        "Расстояние (м)",
        **NULLABLE,
        validators=[MinValueValidator(1)],  # только положительные числа
    )

    class Meta:
        verbose_name = "Расстояние"
        verbose_name_plural = "Расстояния"


class GeneralComfortType(models.Model):
    """Основные удобства."""

    name = models.CharField("Название", max_length=NAME_MAX_LENGTH, unique=True)
    icon = models.ImageField(
        "Иконка",
        upload_to=settings.COMFORT_ICONS_FOLDER,  # подпапка внутри MEDIA_ROOT
        **NULLABLE,
        help_text="Загрузите изображение иконки",
    )

    class Meta:
        verbose_name = "Вид основных удобств"
        verbose_name_plural = "Виды основных удобств"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AmenityType(models.Model):
    """Вид особых удобств."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)  # Тип удобства

    def __str__(self):
        return self.name


class Amenity(models.Model):
    """Особые удобства."""

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    amenity_type = models.ForeignKey(AmenityType, related_name="amenities", on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)  # Галочка
    hotel = models.ForeignKey(
        "Hotel",
        on_delete=models.CASCADE,
        verbose_name="Отель",
        related_name="amenities",
    )

    def __str__(self):
        return f"{self.name} ({self.amenity_type})"


class Rule(models.Model):
    """Правила отеля."""

    hotel = models.ForeignKey("Hotel", related_name="rules", on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    is_checked = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class HotelPhoto(models.Model):
    """Фотографии отеля."""

    hotel = models.ForeignKey("Hotel", related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.HOTEL_PHOTOS_FOLDER)
    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)

    def __str__(self):
        return f"Фото {self.hotel.name}"


class Hotel(models.Model):
    """Отель."""

    HOTEL_TYPES = [
        ("hotel", "Отель"),
        ("hostel", "Хостел"),
        ("villa", "Вилла"),
        ("apartment", "Апартаменты"),
        ("guest", "Гостевой дом"),
    ]

    name = models.CharField("Название отеля", max_length=HOTEL_MAX_LENGTH, unique=True)
    vacation_type = models.ForeignKey(
        VacationType,
        on_delete=models.SET_NULL,
        verbose_name="Тип отдыха",
        related_name="hotels",
        null=True,
    )
    hotel_type = models.CharField(
        "Тип отеля",
        max_length=HOTEL_TYPE_MAX_LENGTH,
        choices=HOTEL_TYPES,
        default="hotel",
    )
    category = models.IntegerField(
        "Категория",
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0,
    )
    country = models.CharField("Страна", max_length=CITY_MAX_LENGTH)
    city = models.CharField("Город", max_length=CITY_MAX_LENGTH)
    address = models.CharField("Адрес", max_length=ADDRESS_MAX_LENGTH)
    latitude = models.DecimalField(
        "Широта",
        max_digits=9,  # ±90.000000 (диапазон широты)
        decimal_places=6,
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
    )
    longitude = models.DecimalField(
        "Долгота",
        max_digits=10,  # ±180.000000
        decimal_places=6,
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
    )
    distances = models.ManyToManyField(
        Distance,
        verbose_name="Расстояния",
        related_name="hotels",
        **NULLABLE,
    )
    general_comfort = models.ManyToManyField(
        GeneralComfortType,
        verbose_name="Основные удобства",
        related_name="hotels",
        **NULLABLE,
    )
    check_in_time = models.TimeField(default=time(14, 0), verbose_name="Заселение")
    check_out_time = models.TimeField(default=time(12, 0), verbose_name="Выезд")
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        ordering = ["name"]

    def __str__(self):
        return self.name
