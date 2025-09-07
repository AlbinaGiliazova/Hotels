from django.contrib import admin

from hotels.models import VacationType


@admin.register(VacationType)
class VacationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
