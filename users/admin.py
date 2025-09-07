from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Регистрация пользователя в админке."""

    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)
