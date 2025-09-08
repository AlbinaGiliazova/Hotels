from django.contrib import admin

from hotels.models import (
    Amenity,
    AmenityType,
    Distance,
    DistanceType,
    GeneralComfortType,
    Hotel,
    HotelPhoto,
    Rule,
    VacationType,
)


@admin.register(VacationType)
class VacationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(DistanceType)
class DistanceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ("distance_type", "value")
    list_filter = ("distance_type",)


@admin.register(GeneralComfortType)
class GeneralComfortTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)


@admin.register(AmenityType)
class AmenityTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "amenity_type", "is_selected", "hotel")
    list_filter = ("amenity_type", "hotel", "is_selected")
    search_fields = ("name",)


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel", "is_checked")
    list_filter = ("hotel", "is_checked")
    search_fields = ("name",)


@admin.register(HotelPhoto)
class HotelPhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel", "image")
    list_filter = ("hotel",)
    search_fields = ("name",)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel_type", "category", "country", "city")
    list_filter = ("hotel_type", "category", "country", "city")
    search_fields = ("name", "address", "country", "city")
    filter_horizontal = ("distances", "general_comfort")
