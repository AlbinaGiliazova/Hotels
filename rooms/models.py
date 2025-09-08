from django.conf import settings
from django.db import models

from food.models import MealType
from rooms.constants import (
    NAME_MAX_LENGTH,
    ROOM_TYPE_MAX_LENGTH,
    RULE_CHOICE_MAX_LENGTH,
)


class Bed(models.Model):
    """Кровати."""

    has_single = models.BooleanField(default=False, verbose_name="Односпальная кровать")
    single_quantity = models.PositiveIntegerField(default=0, verbose_name="Количество односпальных кроватей")

    has_double = models.BooleanField(default=False, verbose_name="Двуспальная кровать")
    double_quantity = models.PositiveIntegerField(default=0, verbose_name="Количество двуспальных кроватей")

    class Meta:
        verbose_name = "Кровати"
        verbose_name_plural = "Кровати"
        ordering = ["id"]

    def __str__(self):
        single = f"Односпальные: {self.single_quantity}" if self.has_single else "Односпальных нет"
        double = f"Двуспальные: {self.double_quantity}" if self.has_double else "Двуспальных нет"
        return f"{single}, {double}, Выбрано: {self.is_selected}"


class GeneralAmenities(models.Model):
    """Общие удобства."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Общие")
    wifi = models.BooleanField(default=False, verbose_name="Бесплатный Wi-Fi")
    sofa = models.BooleanField(default=False, verbose_name="Диван")
    conditioner = models.BooleanField(default=False, verbose_name="Кондиционер")
    heating = models.BooleanField(default=False, verbose_name="Отопление")
    beds = models.BooleanField(default=False, verbose_name="Удобные кровати")
    tv = models.BooleanField(default=False, verbose_name="Телевизор")
    dinnertable = models.BooleanField(default=False, verbose_name="Обеденный стол")
    kitchen = models.BooleanField(default=False, verbose_name="Кухня")
    worktable = models.BooleanField(default=False, verbose_name="Рабочий стол")
    wardrobe = models.BooleanField(default=False, verbose_name="Шкаф или гардероб")
    bar = models.BooleanField(default=False, verbose_name="Мини-бар")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Общие удобства"
        verbose_name_plural = "Общие удобства"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DrinkingAmenities(models.Model):
    """Кофе-станция."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Кофе-станция")
    teapot = models.BooleanField(default=False, verbose_name="Электрический чайник")
    coffee = models.BooleanField(default=False, verbose_name="Кофемашина")
    tea = models.BooleanField(default=False, verbose_name="Чай/кофе")
    dishes = models.BooleanField(default=False, verbose_name="Посуда")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кофе-станция"
        verbose_name_plural = "Кофе-станция"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BathroomAmenities(models.Model):
    """В ванной комнате."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="В ванной комнате")
    bath = models.BooleanField(default=False, verbose_name="Ванна")
    shower = models.BooleanField(default=False, verbose_name="Душ")
    bidet = models.BooleanField(default=False, verbose_name="Биде")
    jakuzzi = models.BooleanField(default=False, verbose_name="Джакузи")
    fan = models.BooleanField(default=False, verbose_name="Фен")
    bathrobe = models.BooleanField(default=False, verbose_name="Халат")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "В ванной комнате"
        verbose_name_plural = "В ванной комнате"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ViewAmenities(models.Model):
    """Вид."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Вид")
    sea = models.BooleanField(default=False, verbose_name="На море")
    pool = models.BooleanField(default=False, verbose_name="На бассейн")
    park = models.BooleanField(default=False, verbose_name="На парк")
    sight = models.BooleanField(default=False, verbose_name="На достопримечательности")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Вид"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CustomGeneralAmenities(models.Model):
    """Дополнительные удобства."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Название")
    is_selected = models.BooleanField(default=False, verbose_name="Выбрано")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Дополнительные удобства"
        verbose_name_plural = "Дополнительные удобства"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CustomDrinkingAmenities(models.Model):
    """Дополнительные удобства напитков."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Название")
    is_selected = models.BooleanField(default=False, verbose_name="Выбрано")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Дополнительные удобства напитков"
        verbose_name_plural = "Дополнительные удобства напитков"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CustomBathroomAmenities(models.Model):
    """Дополнительные удобства в ванной комнате."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Название")
    is_selected = models.BooleanField(default=False, verbose_name="Выбрано")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Дополнительные удобства в ванной комнате"
        verbose_name_plural = "Дополнительные удобства в ванной комнате"
        ordering = ["name"]

    def __str__(self):
        return self.name


class CustomViewAmenities(models.Model):
    """Дополнительные удобства вида."""

    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name="Название")
    is_selected = models.BooleanField(default=False, verbose_name="Выбрано")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Дополнительные удобства вида"
        verbose_name_plural = "Дополнительные удобства вида"
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
    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)

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
    beds = models.ForeignKey(
        Bed,
        on_delete=models.SET_NULL,
        related_name="rooms",
        null=True,
    )

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        ordering = ["id"]

    def __str__(self):
        return f"Номер {self.id}"
