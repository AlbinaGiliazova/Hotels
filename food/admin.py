"""Админка приложения."""

from django.contrib import admin

from food.models import MealType


@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    """Регистрируем тип питания."""

    list_display = ("type", "price")
    list_filter = ("type",)
    search_fields = ("type",)

    # Чтобы на главной странице списка объектов отображалось человекочитаемое название
    def type_display(self, obj):
        return obj.get_type_display()

    type_display.short_description = "Тип питания"
