from datetime import time

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from hotels.constants import (
    ADDRESS_MAX_LENGTH,
    AMENITY_TYPE_MAX_LENGTH,
    CITY_MAX_LENGTH,
    DISTANCE_TYPE_MAX_LENGTH,
    HOTEL_MAX_LENGTH,
    HOTEL_TYPE_MAX_LENGTH,
    NAME_MAX_LENGTH,
    VACATION_TYPE_MAX_LENGTH,
)
from meals.constants import NULLABLE


class VacationType(models.Model):
    """Тип отдыха. Варианты значений задаются в админке."""

    name = models.CharField("Название типа отдыха", max_length=VACATION_TYPE_MAX_LENGTH, unique=True)

    class Meta:
        verbose_name = "Тип отдыха"
        verbose_name_plural = "Типы отдыха"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Distance(models.Model):
    """Расстояние."""

    name = models.CharField("Тип объекта", max_length=DISTANCE_TYPE_MAX_LENGTH, unique=True)
    value = models.PositiveIntegerField(
        "Расстояние (м)",
        **NULLABLE,
        validators=[MinValueValidator(1)],  # только положительные числа
    )
    hotel = models.ForeignKey("Hotel", related_name="distances", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Расстояние"
        verbose_name_plural = "Расстояния"
        ordering = ["id"]

    def __str__(self):
        return self.id


class HotelAmenity(models.Model):
    """Удобства."""

    AMENITY_TYPE = [
        ("general", "Основные"),
        ("room", "В номере"),
        ("common", "Общие"),
        ("sport", "Спорт и отдых"),
        ("children", "Для детей"),
    ]
    amenity_type = models.CharField(
        "Тип удобств",
        max_length=AMENITY_TYPE_MAX_LENGTH,
        choices=AMENITY_TYPE,
        default="general",
    )
    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Название")
    hotel = models.ForeignKey(
        "Hotel",
        on_delete=models.CASCADE,
        verbose_name="Отель",
        related_name="amenities",
    )
    icon = models.ImageField(
        "Иконка",
        upload_to=settings.COMFORT_ICONS_FOLDER,  # подпапка внутри MEDIA_ROOT
        **NULLABLE,
        help_text="Загрузите изображение иконки",
    )

    class Meta:
        verbose_name = "Удобства отеля"
        verbose_name_plural = "Удобства отеля"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Rule(models.Model):
    """Правила отеля."""

    hotel = models.ForeignKey("Hotel", related_name="rules", on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    is_checked = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Правило отеля"
        verbose_name_plural = "Правила отеля"
        ordering = ["name"]

    def __str__(self):
        return self.name


class HotelPhoto(models.Model):
    """Фотографии отеля."""

    hotel = models.ForeignKey("Hotel", related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.HOTEL_PHOTOS_FOLDER)
    description = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)

    class Meta:
        verbose_name = "Фотография отеля"
        verbose_name_plural = "Фотографии отеля"
        ordering = ["hotel__id"]

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
        "Тип размещения",
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
    latitude = models.FloatField(
        "Широта",
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
    )
    longitude = models.FloatField(
        "Долгота",
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
    )
    check_in_time = models.TimeField("Заселение", default=time(14, 0))
    check_out_time = models.TimeField("Выезд", default=time(12, 0))
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        ordering = ["name"]

    def __str__(self):
        return self.name
